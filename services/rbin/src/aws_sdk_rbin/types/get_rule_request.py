"""Generated from Smithy shape ``com.amazonaws.rbin#GetRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rbin.types.rule_identifier


class GetRuleRequest(TypedDict):
    identifier: "aws_sdk_rbin.types.rule_identifier.RuleIdentifier"
    """<p>The unique ID of the retention rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRuleRequest:
    out: GetRuleRequest = {}  # type: ignore[typeddict-item]
    return out
