"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ApplicationTag``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.application_arn
    import aws_sdk_resource_groups.types.application_tag_key

ApplicationTag: TypeAlias = dict[
    "aws_sdk_resource_groups.types.application_tag_key.ApplicationTagKey",
    "aws_sdk_resource_groups.types.application_arn.ApplicationArn",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ApplicationTag) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ApplicationTag:
    out: ApplicationTag = {}
    for key, value in data.items():
        out[key] = value
    return out
