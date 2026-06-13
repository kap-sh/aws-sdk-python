"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.rule_id


class DeleteRuleInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain that where the rule is to be deleted.</p>"""
    identifier: "aws_sdk_datazone.types.rule_id.RuleId"
    """<p>The ID of the rule that is to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRuleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRuleInput:
    out: DeleteRuleInput = {}  # type: ignore[typeddict-item]
    return out
