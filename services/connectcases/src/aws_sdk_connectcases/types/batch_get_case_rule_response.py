"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetCaseRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.batch_get_case_rule_error_list
    import aws_sdk_connectcases.types.batch_get_case_rule_list
    import aws_sdk_connectcases.types.batch_get_case_rule_unprocessed_list


class BatchGetCaseRuleResponse(TypedDict):
    case_rules: (
        "aws_sdk_connectcases.types.batch_get_case_rule_list.BatchGetCaseRuleList"
    )
    """<p>A list of detailed case rule information.</p>"""
    errors: "aws_sdk_connectcases.types.batch_get_case_rule_error_list.BatchGetCaseRuleErrorList"
    """<p>A list of case rule errors.</p>"""
    unprocessed_case_rules: NotRequired[
        "aws_sdk_connectcases.types.batch_get_case_rule_unprocessed_list.BatchGetCaseRuleUnprocessedList"
    ]
    """<p>A list of unprocessed case rule identifiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCaseRuleResponse) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.batch_get_case_rule_list

    out["caseRules"] = (
        aws_sdk_connectcases.types.batch_get_case_rule_list.serialize_json(
            value["case_rules"]
        )
    )
    import aws_sdk_connectcases.types.batch_get_case_rule_error_list

    out["errors"] = (
        aws_sdk_connectcases.types.batch_get_case_rule_error_list.serialize_json(
            value["errors"]
        )
    )
    if "unprocessed_case_rules" in value:
        import aws_sdk_connectcases.types.batch_get_case_rule_unprocessed_list

        out["unprocessedCaseRules"] = (
            aws_sdk_connectcases.types.batch_get_case_rule_unprocessed_list.serialize_json(
                value["unprocessed_case_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetCaseRuleResponse:
    out: BatchGetCaseRuleResponse = {}  # type: ignore[typeddict-item]
    if "caseRules" in data:
        import aws_sdk_connectcases.types.batch_get_case_rule_list

        out["case_rules"] = (
            aws_sdk_connectcases.types.batch_get_case_rule_list.deserialize_json(
                data["caseRules"]
            )
        )
    else:
        raise DeserializationError("BatchGetCaseRuleResponse.case_rules required")
    if "errors" in data:
        import aws_sdk_connectcases.types.batch_get_case_rule_error_list

        out["errors"] = (
            aws_sdk_connectcases.types.batch_get_case_rule_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchGetCaseRuleResponse.errors required")
    if "unprocessedCaseRules" in data:
        import aws_sdk_connectcases.types.batch_get_case_rule_unprocessed_list

        out["unprocessed_case_rules"] = (
            aws_sdk_connectcases.types.batch_get_case_rule_unprocessed_list.deserialize_json(
                data["unprocessedCaseRules"]
            )
        )
    return out
