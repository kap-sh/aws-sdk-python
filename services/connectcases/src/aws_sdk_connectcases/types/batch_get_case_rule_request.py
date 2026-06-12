"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetCaseRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_rule_identifier_list
    import aws_sdk_connectcases.types.domain_id


class BatchGetCaseRuleRequest(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>Unique identifier of a Cases domain.</p>"""
    case_rules: (
        "aws_sdk_connectcases.types.case_rule_identifier_list.CaseRuleIdentifierList"
    )
    """<p>A list of case rule identifiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCaseRuleRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.case_rule_identifier_list

    out["caseRules"] = (
        aws_sdk_connectcases.types.case_rule_identifier_list.serialize_json(
            value["case_rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetCaseRuleRequest:
    out: BatchGetCaseRuleRequest = {}  # type: ignore[typeddict-item]
    if "caseRules" in data:
        import aws_sdk_connectcases.types.case_rule_identifier_list

        out["case_rules"] = (
            aws_sdk_connectcases.types.case_rule_identifier_list.deserialize_json(
                data["caseRules"]
            )
        )
    else:
        raise DeserializationError("BatchGetCaseRuleRequest.case_rules required")
    return out
