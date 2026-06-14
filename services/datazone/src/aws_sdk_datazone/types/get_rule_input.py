"""Generated from Smithy shape ``com.amazonaws.datazone#GetRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.revision
    import aws_sdk_datazone.types.rule_id


class GetRuleInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the <code>GetRule</code> action is to be invoked.</p>"""
    identifier: "aws_sdk_datazone.types.rule_id.RuleId"
    """<p>The ID of the rule.</p>"""
    revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRuleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRuleInput:
    out: GetRuleInput = {}  # type: ignore[typeddict-item]
    return out
