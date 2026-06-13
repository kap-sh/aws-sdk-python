"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_snow_device_management.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.tag_map


class TagResourceInput(TypedDict):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the device or task.</p>"""
    tags: "aws_sdk_snow_device_management.types.tag_map.TagMap"
    """<p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_snow_device_management.types.tag_map

    out["tags"] = aws_sdk_snow_device_management.types.tag_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_snow_device_management.types.tag_map

        out["tags"] = aws_sdk_snow_device_management.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
