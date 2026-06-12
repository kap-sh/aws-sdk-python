"""Generated from Smithy shape ``com.amazonaws.greengrassv2#Component``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.component_arn
    import aws_sdk_greengrassv2.types.component_latest_version
    import aws_sdk_greengrassv2.types.component_name_string


class Component(TypedDict):
    arn: NotRequired["aws_sdk_greengrassv2.types.component_arn.ComponentARN"]
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the component version.</p>"""
    component_name: NotRequired[
        "aws_sdk_greengrassv2.types.component_name_string.ComponentNameString"
    ]
    """<p>The name of the component.</p>"""
    latest_version: NotRequired[
        "aws_sdk_greengrassv2.types.component_latest_version.ComponentLatestVersion"
    ]
    """<p>The latest version of the component and its details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Component) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "latest_version" in value:
        import aws_sdk_greengrassv2.types.component_latest_version

        out["latestVersion"] = (
            aws_sdk_greengrassv2.types.component_latest_version.serialize_json(
                value["latest_version"]
            )
        )
    return out


def deserialize_json(data: dict) -> Component:
    out: Component = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    if "latestVersion" in data:
        import aws_sdk_greengrassv2.types.component_latest_version

        out["latest_version"] = (
            aws_sdk_greengrassv2.types.component_latest_version.deserialize_json(
                data["latestVersion"]
            )
        )
    return out
