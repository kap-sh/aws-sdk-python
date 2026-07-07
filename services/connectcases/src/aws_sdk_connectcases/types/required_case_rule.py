"""Generated from Smithy shape ``com.amazonaws.connectcases#RequiredCaseRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.boolean_condition_list


class RequiredCaseRule(TypedDict, closed=True):
    default_value: "bool"
    """<p>The value of the rule (that is, whether the field is required) should none of the conditions evaluate to true.</p>"""
    conditions: "aws_sdk_connectcases.types.boolean_condition_list.BooleanConditionList"
    """<p>List of conditions for the required rule; the first condition to evaluate to true dictates the value of the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequiredCaseRule) -> dict:
    out: dict = {}
    out["defaultValue"] = value["default_value"]
    import aws_sdk_connectcases.types.boolean_condition_list

    out["conditions"] = (
        aws_sdk_connectcases.types.boolean_condition_list.serialize_json(
            value["conditions"]
        )
    )
    return out


def deserialize_json(data: dict) -> RequiredCaseRule:
    out: RequiredCaseRule = {}  # type: ignore[typeddict-item]
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    else:
        raise DeserializationError("RequiredCaseRule.default_value required")
    if "conditions" in data:
        import aws_sdk_connectcases.types.boolean_condition_list

        out["conditions"] = (
            aws_sdk_connectcases.types.boolean_condition_list.deserialize_json(
                data["conditions"]
            )
        )
    else:
        raise DeserializationError("RequiredCaseRule.conditions required")
    return out
