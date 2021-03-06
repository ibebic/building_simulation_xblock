"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment


class BuildingSimulationXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    display_name = String(display_name="Display Name",
                          default="Building Simulation",
                          scope=Scope.settings,
                          help="This name appears in the horizontal navigation at the top of the page.")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the CommunityEyesXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/building_simulation.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/building_simulation.css"))
        frag.add_css(self.resource_string("static/css/content.css"))
        frag.add_css(self.resource_string("static/css/progress.css"))
        frag.add_css(self.resource_string("static/css/style.css"))
        frag.add_css(self.resource_string("static/css/tooltip.css"))

        frag.add_javascript(self.resource_string("static/js/lib/three.js"))
        frag.add_javascript(self.resource_string("static/js/lib/Detector.js"))
        frag.add_javascript(self.resource_string("static/js/lib/OrbitControls.example.js"))
        frag.add_javascript(self.resource_string("static/js/lib/numeral.min.js"))
        frag.add_javascript(self.resource_string("static/js/lib/stateBuffer.js"))

        frag.add_javascript(self.resource_string("static/js/src/building_simulation.js"))
        frag.add_javascript(self.resource_string("static/js/src/sceneModel.js"))
        frag.add_javascript(self.resource_string("static/js/src/calc.js"))
        frag.add_javascript(self.resource_string("static/js/src/clickEvents.js"))
        frag.add_javascript(self.resource_string("static/js/src/earth.js"))

        frag.initialize_js('BuildingSimulationXBlock')
        return frag


    def studio_view(self, context):
        """
        Create a fragment used to display the edit view in the Studio.
        """
        html_str = pkg_resources.resource_string(__name__, "static/html/studio_view.html")
        frag = Fragment(unicode(html_str).format(
                                                    display_name=self.display_name,
                                                    display_description=self.display_description,
                                                    thumbnail_url=self.thumbnail_url
                                                ))
        js_str = pkg_resources.resource_string(__name__, "static/js/src/studio_edit.js")
        frag.add_javascript(unicode(js_str))
        frag.initialize_js('StudioEdit')
        return frag

    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """
        Called when submitting the form in Studio.
        """
        self.display_name = data.get('display_name')
        self.display_description = data.get('display_description')
        self.thumbnail_url = data.get('thumbnail_url')

        return {'result': 'success'}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("BuildingSimulationXBlock",
             """<building_simulation/>
             """),
            ("Multiple BuildingSimulationXBlock",
             """<vertical_demo>
                <building_simulation/>
                <building_simulation/>
                <building_simulation/>
                </vertical_demo>
             """),
        ]
