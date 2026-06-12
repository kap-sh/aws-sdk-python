"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatefulRulesHeaderDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class RuleGroupSourceStatefulRulesHeaderDetails(TypedDict):
    destination: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The destination IP address or address range to inspect for, in CIDR notation. To match with any address, specify <code>ANY</code>.</p>"""
    destination_port: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The destination port to inspect for. You can specify an individual port, such as <code>1994</code>. You also can specify a port range, such as <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p>"""
    direction: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The direction of traffic flow to inspect. If set to <code>ANY</code>, the inspection matches bidirectional traffic, both from the source to the destination and from the destination to the source. If set to <code>FORWARD</code>, the inspection only matches traffic going from the source to the destination.</p>"""
    protocol: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The protocol to inspect for. To inspector for all protocols, use <code>IP</code>.</p>"""
    source: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The source IP address or address range to inspect for, in CIDR notation. To match with any address, specify <code>ANY</code>.</p>"""
    source_port: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The source port to inspect for. You can specify an individual port, such as <code>1994</code>. You also can specify a port range, such as <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceStatefulRulesHeaderDetails) -> dict:
    out: dict = {}
    if "destination" in value:
        out["Destination"] = value["destination"]
    if "destination_port" in value:
        out["DestinationPort"] = value["destination_port"]
    if "direction" in value:
        out["Direction"] = value["direction"]
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "source" in value:
        out["Source"] = value["source"]
    if "source_port" in value:
        out["SourcePort"] = value["source_port"]
    return out


def deserialize_json(data: dict) -> RuleGroupSourceStatefulRulesHeaderDetails:
    out: RuleGroupSourceStatefulRulesHeaderDetails = {}  # type: ignore[typeddict-item]
    if "Destination" in data:
        out["destination"] = data["Destination"]
    if "DestinationPort" in data:
        out["destination_port"] = data["DestinationPort"]
    if "Direction" in data:
        out["direction"] = data["Direction"]
    if "Protocol" in data:
        out["protocol"] = data["Protocol"]
    if "Source" in data:
        out["source"] = data["Source"]
    if "SourcePort" in data:
        out["source_port"] = data["SourcePort"]
    return out
