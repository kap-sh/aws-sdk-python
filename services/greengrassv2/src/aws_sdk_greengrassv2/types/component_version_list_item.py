"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentVersionListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.component_name_string
    import aws_sdk_greengrassv2.types.component_version_string
    import aws_sdk_greengrassv2.types.non_empty_string


class ComponentVersionListItem(TypedDict):
    component_name: NotRequired[
        "aws_sdk_greengrassv2.types.component_name_string.ComponentNameString"
    ]
    """<p>The name of the component.</p>"""
    component_version: NotRequired[
        "aws_sdk_greengrassv2.types.component_version_string.ComponentVersionString"
    ]
    """<p>The version of the component.</p>"""
    arn: NotRequired["aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the component version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentVersionListItem) -> dict:
    out: dict = {}
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_version" in value:
        out["componentVersion"] = value["component_version"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> ComponentVersionListItem:
    out: ComponentVersionListItem = {}  # type: ignore[typeddict-item]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    if "componentVersion" in data:
        out["component_version"] = data["componentVersion"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
