"""Generated from Smithy shape ``com.amazonaws.qconnect#TagFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.and_conditions
    import capo_qconnect.types.or_conditions
    import capo_qconnect.types.tag_condition


class _TagFilter_tagCondition(TypedDict, closed=True):
    tagCondition: "capo_qconnect.types.tag_condition.TagCondition"


class _TagFilter_andConditions(TypedDict, closed=True):
    andConditions: "capo_qconnect.types.and_conditions.AndConditions"


class _TagFilter_orConditions(TypedDict, closed=True):
    orConditions: "capo_qconnect.types.or_conditions.OrConditions"


TagFilter: TypeAlias = (
    _TagFilter_tagCondition | _TagFilter_andConditions | _TagFilter_orConditions
)


# --- restJson1 ser/de ---
def serialize_json(value: TagFilter) -> dict:
    if "tagCondition" in value:
        import capo_qconnect.types.tag_condition

        return {
            "tagCondition": capo_qconnect.types.tag_condition.serialize_json(
                value["tagCondition"]
            )
        }
    elif "andConditions" in value:
        import capo_qconnect.types.and_conditions

        return {
            "andConditions": capo_qconnect.types.and_conditions.serialize_json(
                value["andConditions"]
            )
        }
    elif "orConditions" in value:
        import capo_qconnect.types.or_conditions

        return {
            "orConditions": capo_qconnect.types.or_conditions.serialize_json(
                value["orConditions"]
            )
        }
    else:
        raise SerializationError("TagFilter: no variant present")


def deserialize_json(data: dict) -> TagFilter:
    if "tagCondition" in data:
        import capo_qconnect.types.tag_condition

        return {
            "tagCondition": capo_qconnect.types.tag_condition.deserialize_json(
                data["tagCondition"]
            )
        }
    elif "andConditions" in data:
        import capo_qconnect.types.and_conditions

        return {
            "andConditions": capo_qconnect.types.and_conditions.deserialize_json(
                data["andConditions"]
            )
        }
    elif "orConditions" in data:
        import capo_qconnect.types.or_conditions

        return {
            "orConditions": capo_qconnect.types.or_conditions.deserialize_json(
                data["orConditions"]
            )
        }
    else:
        raise DeserializationError("TagFilter: no recognized variant key")
