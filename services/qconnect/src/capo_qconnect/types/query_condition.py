"""Generated from Smithy shape ``com.amazonaws.qconnect#QueryCondition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.query_condition_item


class _QueryCondition_single(TypedDict, closed=True):
    single: "capo_qconnect.types.query_condition_item.QueryConditionItem"


QueryCondition: TypeAlias = _QueryCondition_single


# --- restJson1 ser/de ---
def serialize_json(value: QueryCondition) -> dict:
    if "single" in value:
        import capo_qconnect.types.query_condition_item

        return {
            "single": capo_qconnect.types.query_condition_item.serialize_json(
                value["single"]
            )
        }
    else:
        raise SerializationError("QueryCondition: no variant present")


def deserialize_json(data: dict) -> QueryCondition:
    if "single" in data:
        import capo_qconnect.types.query_condition_item

        return {
            "single": capo_qconnect.types.query_condition_item.deserialize_json(
                data["single"]
            )
        }
    else:
        raise DeserializationError("QueryCondition: no recognized variant key")
