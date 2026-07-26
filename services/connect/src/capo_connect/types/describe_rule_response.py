"""Generated from Smithy shape ``com.amazonaws.connect#DescribeRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.rule


class DescribeRuleResponse(TypedDict, closed=True):
    rule: "capo_connect.types.rule.Rule"
    """<p>Information about the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRuleResponse) -> dict:
    out: dict = {}
    import capo_connect.types.rule

    out["Rule"] = capo_connect.types.rule.serialize_json(value["rule"])
    return out


def deserialize_json(data: dict) -> DescribeRuleResponse:
    out: DescribeRuleResponse = {}  # type: ignore[typeddict-item]
    if "Rule" in data:
        import capo_connect.types.rule

        out["rule"] = capo_connect.types.rule.deserialize_json(data["Rule"])
    else:
        raise DeserializationError("DescribeRuleResponse.rule required")
    return out
