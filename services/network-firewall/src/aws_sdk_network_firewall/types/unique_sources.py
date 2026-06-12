"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UniqueSources``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.count


class UniqueSources(TypedDict):
    count: "aws_sdk_network_firewall.types.count.Count"
    """<p>The number of unique source IP addresses that connected to a domain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UniqueSources) -> dict:
    out: dict = {}
    out["Count"] = value.get("count", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> UniqueSources:
    out: UniqueSources = {}  # type: ignore[typeddict-item]
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    return out
