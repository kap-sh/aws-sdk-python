"""Generated from Smithy shape ``com.amazonaws.connectcases#HiddenCaseRule``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.boolean_condition_list


class HiddenCaseRule(TypedDict):
    default_value: "bool"
    """<p>Whether the field is hidden when no conditions match.</p>"""
    conditions: "aws_sdk_connectcases.types.boolean_condition_list.BooleanConditionList"
    """<p>A list of conditions that determine field visibility.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HiddenCaseRule) -> dict:
    out: dict = {}
    out["defaultValue"] = value["default_value"]
    import aws_sdk_connectcases.types.boolean_condition_list

    out["conditions"] = (
        aws_sdk_connectcases.types.boolean_condition_list.serialize_json(
            value["conditions"]
        )
    )
    return out


def deserialize_json(data: dict) -> HiddenCaseRule:
    out: HiddenCaseRule = {}  # type: ignore[typeddict-item]
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    else:
        raise DeserializationError("HiddenCaseRule.default_value required")
    if "conditions" in data:
        import aws_sdk_connectcases.types.boolean_condition_list

        out["conditions"] = (
            aws_sdk_connectcases.types.boolean_condition_list.deserialize_json(
                data["conditions"]
            )
        )
    else:
        raise DeserializationError("HiddenCaseRule.conditions required")
    return out
