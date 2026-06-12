"""Generated from Smithy shape ``com.amazonaws.kafka#VpcConnectivityScram``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean


class VpcConnectivityScram(TypedDict):
    enabled: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>SASL/SCRAM authentication is on or off for VPC connectivity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConnectivityScram) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> VpcConnectivityScram:
    out: VpcConnectivityScram = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
