"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteRulesetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.ruleset_name


class DeleteRulesetRequest(TypedDict, closed=True):
    name: "capo_databrew.types.ruleset_name.RulesetName"
    """<p>The name of the ruleset to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRulesetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRulesetRequest:
    out: DeleteRulesetRequest = {}  # type: ignore[typeddict-item]
    return out
