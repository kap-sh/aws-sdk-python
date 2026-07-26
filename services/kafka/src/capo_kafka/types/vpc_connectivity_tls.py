"""Generated from Smithy shape ``com.amazonaws.kafka#VpcConnectivityTls``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__boolean


class VpcConnectivityTls(TypedDict, closed=True):
    enabled: NotRequired["capo_kafka.types.__boolean.__boolean"]
    """<p>TLS authentication is on or off for VPC connectivity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConnectivityTls) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> VpcConnectivityTls:
    out: VpcConnectivityTls = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
