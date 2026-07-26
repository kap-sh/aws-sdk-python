"""Generated from Smithy shape ``com.amazonaws.servicediscovery#SOA``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.record_ttl


class SOA(TypedDict, closed=True):
    ttl: "capo_servicediscovery.types.record_ttl.RecordTTL"
    """<p>The time to live (TTL) for purposes of negative caching.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SOA) -> dict:
    out: dict = {}
    out["TTL"] = value["ttl"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SOA:
    out: SOA = {}  # type: ignore[typeddict-item]
    if "TTL" in data:
        out["ttl"] = data["TTL"]
    else:
        raise DeserializationError("SOA.ttl required")
    return out
