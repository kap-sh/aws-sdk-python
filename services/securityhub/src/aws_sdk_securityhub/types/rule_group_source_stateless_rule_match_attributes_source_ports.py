"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleMatchAttributesSourcePorts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer


class RuleGroupSourceStatelessRuleMatchAttributesSourcePorts(TypedDict, closed=True):
    from_port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The starting port value for the port range.</p>"""
    to_port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The ending port value for the port range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: RuleGroupSourceStatelessRuleMatchAttributesSourcePorts,
) -> dict:
    out: dict = {}
    if "from_port" in value:
        out["FromPort"] = value["from_port"]
    if "to_port" in value:
        out["ToPort"] = value["to_port"]
    return out


def deserialize_json(
    data: dict,
) -> RuleGroupSourceStatelessRuleMatchAttributesSourcePorts:
    out: RuleGroupSourceStatelessRuleMatchAttributesSourcePorts = {}  # type: ignore[typeddict-item]
    if "FromPort" in data:
        out["from_port"] = data["FromPort"]
    if "ToPort" in data:
        out["to_port"] = data["ToPort"]
    return out
