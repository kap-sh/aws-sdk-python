"""Generated from Smithy shape ``com.amazonaws.connectcases#TagFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcases.types.tag_value


class _TagFilter_equalTo(TypedDict, closed=True):
    equalTo: "capo_connectcases.types.tag_value.TagValue"


TagFilter: TypeAlias = _TagFilter_equalTo


# --- restJson1 ser/de ---
def serialize_json(value: TagFilter) -> dict:
    if "equalTo" in value:
        import capo_connectcases.types.tag_value

        return {
            "equalTo": capo_connectcases.types.tag_value.serialize_json(
                value["equalTo"]
            )
        }
    else:
        raise SerializationError("TagFilter: no variant present")


def deserialize_json(data: dict) -> TagFilter:
    if "equalTo" in data:
        import capo_connectcases.types.tag_value

        return {
            "equalTo": capo_connectcases.types.tag_value.deserialize_json(
                data["equalTo"]
            )
        }
    else:
        raise DeserializationError("TagFilter: no recognized variant key")
