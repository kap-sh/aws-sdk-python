"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseRuleDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcases.types.field_options_case_rule
    import capo_connectcases.types.hidden_case_rule
    import capo_connectcases.types.required_case_rule


class _CaseRuleDetails_required(TypedDict, closed=True):
    required: "capo_connectcases.types.required_case_rule.RequiredCaseRule"


class _CaseRuleDetails_fieldOptions(TypedDict, closed=True):
    fieldOptions: "capo_connectcases.types.field_options_case_rule.FieldOptionsCaseRule"


class _CaseRuleDetails_hidden(TypedDict, closed=True):
    hidden: "capo_connectcases.types.hidden_case_rule.HiddenCaseRule"


CaseRuleDetails: TypeAlias = (
    _CaseRuleDetails_required | _CaseRuleDetails_fieldOptions | _CaseRuleDetails_hidden
)


# --- restJson1 ser/de ---
def serialize_json(value: CaseRuleDetails) -> dict:
    if "required" in value:
        import capo_connectcases.types.required_case_rule

        return {
            "required": capo_connectcases.types.required_case_rule.serialize_json(
                value["required"]
            )
        }
    elif "fieldOptions" in value:
        import capo_connectcases.types.field_options_case_rule

        return {
            "fieldOptions": capo_connectcases.types.field_options_case_rule.serialize_json(
                value["fieldOptions"]
            )
        }
    elif "hidden" in value:
        import capo_connectcases.types.hidden_case_rule

        return {
            "hidden": capo_connectcases.types.hidden_case_rule.serialize_json(
                value["hidden"]
            )
        }
    else:
        raise SerializationError("CaseRuleDetails: no variant present")


def deserialize_json(data: dict) -> CaseRuleDetails:
    if "required" in data:
        import capo_connectcases.types.required_case_rule

        return {
            "required": capo_connectcases.types.required_case_rule.deserialize_json(
                data["required"]
            )
        }
    elif "fieldOptions" in data:
        import capo_connectcases.types.field_options_case_rule

        return {
            "fieldOptions": capo_connectcases.types.field_options_case_rule.deserialize_json(
                data["fieldOptions"]
            )
        }
    elif "hidden" in data:
        import capo_connectcases.types.hidden_case_rule

        return {
            "hidden": capo_connectcases.types.hidden_case_rule.deserialize_json(
                data["hidden"]
            )
        }
    else:
        raise DeserializationError("CaseRuleDetails: no recognized variant key")
