"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentCandidate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.component_name_string
    import aws_sdk_greengrassv2.types.component_version_requirement_map
    import aws_sdk_greengrassv2.types.component_version_string


class ComponentCandidate(TypedDict):
    component_name: NotRequired[
        "aws_sdk_greengrassv2.types.component_name_string.ComponentNameString"
    ]
    """<p>The name of the component.</p>"""
    component_version: NotRequired[
        "aws_sdk_greengrassv2.types.component_version_string.ComponentVersionString"
    ]
    """<p>The version of the component.</p>"""
    version_requirements: NotRequired[
        "aws_sdk_greengrassv2.types.component_version_requirement_map.ComponentVersionRequirementMap"
    ]
    r"""<p>The version requirements for the component's dependencies. Greengrass core devices get the version requirements from component recipes.</p> <p>IoT Greengrass V2 uses semantic version constraints. For more information, see <a href=\"https://semver.org/\">Semantic Versioning</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentCandidate) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_version" in value:
        out["componentVersion"] = value["component_version"]
    if "version_requirements" in value:
        import aws_sdk_greengrassv2.types.component_version_requirement_map

        out["versionRequirements"] = (
            aws_sdk_greengrassv2.types.component_version_requirement_map.serialize_json(
                value["version_requirements"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentCandidate:
    out: ComponentCandidate = {}  # type: ignore[typeddict-item]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    if "componentVersion" in data:
        out["component_version"] = data["componentVersion"]
    if "versionRequirements" in data:
        import aws_sdk_greengrassv2.types.component_version_requirement_map

        out["version_requirements"] = (
            aws_sdk_greengrassv2.types.component_version_requirement_map.deserialize_json(
                data["versionRequirements"]
            )
        )
    return out
