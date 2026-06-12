"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentDependencyRequirement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.component_dependency_type
    import aws_sdk_greengrassv2.types.non_empty_string


class ComponentDependencyRequirement(TypedDict):
    version_requirement: NotRequired[
        "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The component version requirement for the component dependency.</p> <p>IoT Greengrass V2 uses semantic version constraints. For more information, see <a href=\"https://semver.org/\">Semantic Versioning</a>.</p>"""
    dependency_type: NotRequired[
        "aws_sdk_greengrassv2.types.component_dependency_type.ComponentDependencyType"
    ]
    """<p>The type of this dependency. Choose from the following options:</p> <ul> <li> <p> <code>SOFT</code> – The component doesn't restart if the dependency changes state.</p> </li> <li> <p> <code>HARD</code> – The component restarts if the dependency changes state.</p> </li> </ul> <p>Default: <code>HARD</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentDependencyRequirement) -> dict:
    out: dict = {}
    if "version_requirement" in value:
        out["versionRequirement"] = value["version_requirement"]
    if "dependency_type" in value:
        import aws_sdk_greengrassv2.types.component_dependency_type

        out["dependencyType"] = (
            aws_sdk_greengrassv2.types.component_dependency_type.serialize_json(
                value["dependency_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentDependencyRequirement:
    out: ComponentDependencyRequirement = {}  # type: ignore[typeddict-item]
    if "versionRequirement" in data:
        out["version_requirement"] = data["versionRequirement"]
    if "dependencyType" in data:
        import aws_sdk_greengrassv2.types.component_dependency_type

        out["dependency_type"] = (
            aws_sdk_greengrassv2.types.component_dependency_type.deserialize_json(
                data["dependencyType"]
            )
        )
    return out
