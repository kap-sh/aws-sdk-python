"""Generated from Smithy shape ``com.amazonaws.qconnect#OrCondition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.and_conditions
    import capo_qconnect.types.tag_condition


class _OrCondition_andConditions(TypedDict, closed=True):
    andConditions: "capo_qconnect.types.and_conditions.AndConditions"


class _OrCondition_tagCondition(TypedDict, closed=True):
    tagCondition: "capo_qconnect.types.tag_condition.TagCondition"


OrCondition: TypeAlias = _OrCondition_andConditions | _OrCondition_tagCondition


# --- restJson1 ser/de ---
def serialize_json(value: OrCondition) -> dict:
    if "andConditions" in value:
        import capo_qconnect.types.and_conditions

        return {
            "andConditions": capo_qconnect.types.and_conditions.serialize_json(
                value["andConditions"]
            )
        }
    elif "tagCondition" in value:
        import capo_qconnect.types.tag_condition

        return {
            "tagCondition": capo_qconnect.types.tag_condition.serialize_json(
                value["tagCondition"]
            )
        }
    else:
        raise SerializationError("OrCondition: no variant present")


def deserialize_json(data: dict) -> OrCondition:
    if "andConditions" in data:
        import capo_qconnect.types.and_conditions

        return {
            "andConditions": capo_qconnect.types.and_conditions.deserialize_json(
                data["andConditions"]
            )
        }
    elif "tagCondition" in data:
        import capo_qconnect.types.tag_condition

        return {
            "tagCondition": capo_qconnect.types.tag_condition.deserialize_json(
                data["tagCondition"]
            )
        }
    else:
        raise DeserializationError("OrCondition: no recognized variant key")
