"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentPlatform``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.non_empty_string
    import aws_sdk_greengrassv2.types.platform_attributes_map


class ComponentPlatform(TypedDict):
    name: NotRequired["aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>The friendly name of the platform. This name helps you identify the platform.</p> <p>If you omit this parameter, IoT Greengrass creates a friendly name from the <code>os</code> and <code>architecture</code> of the platform.</p>"""
    attributes: NotRequired[
        "aws_sdk_greengrassv2.types.platform_attributes_map.PlatformAttributesMap"
    ]
    r"""<p>A dictionary of attributes for the platform. The IoT Greengrass Core software defines the <code>os</code> and <code>architecture</code> by default. You can specify additional platform attributes for a core device when you deploy the Greengrass nucleus component. For more information, see the <a href=\"https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-nucleus-component.html\">Greengrass nucleus component</a> in the <i>IoT Greengrass V2 Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentPlatform) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "attributes" in value:
        import aws_sdk_greengrassv2.types.platform_attributes_map

        out["attributes"] = (
            aws_sdk_greengrassv2.types.platform_attributes_map.serialize_json(
                value["attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentPlatform:
    out: ComponentPlatform = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "attributes" in data:
        import aws_sdk_greengrassv2.types.platform_attributes_map

        out["attributes"] = (
            aws_sdk_greengrassv2.types.platform_attributes_map.deserialize_json(
                data["attributes"]
            )
        )
    return out
