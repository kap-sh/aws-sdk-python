"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Hits``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.count


class Hits(TypedDict, closed=True):
    count: "capo_network_firewall.types.count.Count"
    """<p>The number of attempts made to access a domain.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Hits) -> dict:
    out: dict = {}
    out["Count"] = value.get("count", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> Hits:
    out: Hits = {}  # type: ignore[typeddict-item]
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    return out
