"""Generated from Smithy shape ``com.amazonaws.connectcases#CompoundCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.boolean_condition_list


class CompoundCondition(TypedDict, closed=True):
    conditions: "aws_sdk_connectcases.types.boolean_condition_list.BooleanConditionList"
    """<p>The list of conditions to combine using the logical operator.</p> <note> <p>For API users: A case rule can have a maximum of 5 conditions, spread across a maximum of 2 levels of nesting.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompoundCondition) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.boolean_condition_list

    out["conditions"] = (
        aws_sdk_connectcases.types.boolean_condition_list.serialize_json(
            value["conditions"]
        )
    )
    return out


def deserialize_json(data: dict) -> CompoundCondition:
    out: CompoundCondition = {}  # type: ignore[typeddict-item]
    if "conditions" in data:
        import aws_sdk_connectcases.types.boolean_condition_list

        out["conditions"] = (
            aws_sdk_connectcases.types.boolean_condition_list.deserialize_json(
                data["conditions"]
            )
        )
    else:
        raise DeserializationError("CompoundCondition.conditions required")
    return out
