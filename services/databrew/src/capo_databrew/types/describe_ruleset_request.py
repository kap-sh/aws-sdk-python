"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeRulesetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.ruleset_name


class DescribeRulesetRequest(TypedDict, closed=True):
    name: "capo_databrew.types.ruleset_name.RulesetName"
    """<p>The name of the ruleset to be described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRulesetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRulesetRequest:
    out: DescribeRulesetRequest = {}  # type: ignore[typeddict-item]
    return out
