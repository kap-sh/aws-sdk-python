"""Generated from Smithy shape ``com.amazonaws.rbin#UnlockRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rbin.types.rule_identifier


class UnlockRuleRequest(TypedDict, closed=True):
    identifier: "capo_rbin.types.rule_identifier.RuleIdentifier"
    """<p>The unique ID of the retention rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnlockRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UnlockRuleRequest:
    out: UnlockRuleRequest = {}  # type: ignore[typeddict-item]
    return out
