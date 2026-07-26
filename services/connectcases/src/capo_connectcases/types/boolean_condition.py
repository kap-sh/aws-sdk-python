"""Generated from Smithy shape ``com.amazonaws.connectcases#BooleanCondition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcases.types.boolean_operands
    import capo_connectcases.types.compound_condition


class _BooleanCondition_equalTo(TypedDict, closed=True):
    equalTo: "capo_connectcases.types.boolean_operands.BooleanOperands"


class _BooleanCondition_notEqualTo(TypedDict, closed=True):
    notEqualTo: "capo_connectcases.types.boolean_operands.BooleanOperands"


class _BooleanCondition_andAll(TypedDict, closed=True):
    andAll: "capo_connectcases.types.compound_condition.CompoundCondition"


class _BooleanCondition_orAll(TypedDict, closed=True):
    orAll: "capo_connectcases.types.compound_condition.CompoundCondition"


BooleanCondition: TypeAlias = (
    _BooleanCondition_equalTo
    | _BooleanCondition_notEqualTo
    | _BooleanCondition_andAll
    | _BooleanCondition_orAll
)


# --- restJson1 ser/de ---
def serialize_json(value: BooleanCondition) -> dict:
    if "equalTo" in value:
        import capo_connectcases.types.boolean_operands

        return {
            "equalTo": capo_connectcases.types.boolean_operands.serialize_json(
                value["equalTo"]
            )
        }
    elif "notEqualTo" in value:
        import capo_connectcases.types.boolean_operands

        return {
            "notEqualTo": capo_connectcases.types.boolean_operands.serialize_json(
                value["notEqualTo"]
            )
        }
    elif "andAll" in value:
        import capo_connectcases.types.compound_condition

        return {
            "andAll": capo_connectcases.types.compound_condition.serialize_json(
                value["andAll"]
            )
        }
    elif "orAll" in value:
        import capo_connectcases.types.compound_condition

        return {
            "orAll": capo_connectcases.types.compound_condition.serialize_json(
                value["orAll"]
            )
        }
    else:
        raise SerializationError("BooleanCondition: no variant present")


def deserialize_json(data: dict) -> BooleanCondition:
    if "equalTo" in data:
        import capo_connectcases.types.boolean_operands

        return {
            "equalTo": capo_connectcases.types.boolean_operands.deserialize_json(
                data["equalTo"]
            )
        }
    elif "notEqualTo" in data:
        import capo_connectcases.types.boolean_operands

        return {
            "notEqualTo": capo_connectcases.types.boolean_operands.deserialize_json(
                data["notEqualTo"]
            )
        }
    elif "andAll" in data:
        import capo_connectcases.types.compound_condition

        return {
            "andAll": capo_connectcases.types.compound_condition.deserialize_json(
                data["andAll"]
            )
        }
    elif "orAll" in data:
        import capo_connectcases.types.compound_condition

        return {
            "orAll": capo_connectcases.types.compound_condition.deserialize_json(
                data["orAll"]
            )
        }
    else:
        raise DeserializationError("BooleanCondition: no recognized variant key")
