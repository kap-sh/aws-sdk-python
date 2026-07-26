"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer


class RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts(
    TypedDict, closed=True
):
    from_port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The starting port value for the port range.</p>"""
    to_port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The ending port value for the port range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts,
) -> dict:
    out: dict = {}
    if "from_port" in value:
        out["FromPort"] = value["from_port"]
    if "to_port" in value:
        out["ToPort"] = value["to_port"]
    return out


def deserialize_json(
    data: dict,
) -> RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts:
    out: RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts = {}  # type: ignore[typeddict-item]
    if "FromPort" in data:
        out["from_port"] = data["FromPort"]
    if "ToPort" in data:
        out["to_port"] = data["ToPort"]
    return out
