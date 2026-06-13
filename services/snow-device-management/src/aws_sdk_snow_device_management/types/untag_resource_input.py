"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#UntagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.tag_keys


class UntagResourceInput(TypedDict):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the device or task.</p>"""
    tag_keys: "aws_sdk_snow_device_management.types.tag_keys.TagKeys"
    """<p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out
