"""Generated from Smithy shape ``com.amazonaws.connectcases#TagFilter``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.tag_value


class _TagFilter_equalTo(TypedDict):
    equalTo: "aws_sdk_connectcases.types.tag_value.TagValue"


TagFilter: TypeAlias = _TagFilter_equalTo


# --- restJson1 ser/de ---
def serialize_json(value: TagFilter) -> dict:
    if "equalTo" in value:
        import aws_sdk_connectcases.types.tag_value

        return {
            "equalTo": aws_sdk_connectcases.types.tag_value.serialize_json(
                value["equalTo"]
            )
        }
    else:
        raise SerializationError("TagFilter: no variant present")


def deserialize_json(data: dict) -> TagFilter:
    if "equalTo" in data:
        import aws_sdk_connectcases.types.tag_value

        return {
            "equalTo": aws_sdk_connectcases.types.tag_value.deserialize_json(
                data["equalTo"]
            )
        }
    else:
        raise DeserializationError("TagFilter: no recognized variant key")
