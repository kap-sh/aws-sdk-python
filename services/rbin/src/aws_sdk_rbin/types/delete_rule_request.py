"""Generated from Smithy shape ``com.amazonaws.rbin#DeleteRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_rbin.types.rule_identifier


class DeleteRuleRequest(TypedDict, closed=True):
    identifier: "aws_sdk_rbin.types.rule_identifier.RuleIdentifier"
    """<p>The unique ID of the retention rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRuleRequest:
    out: DeleteRuleRequest = {}  # type: ignore[typeddict-item]
    return out
