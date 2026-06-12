"""Generated from Smithy shape ``com.amazonaws.kafka#VpcConnectivityIam``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean


class VpcConnectivityIam(TypedDict):
    enabled: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>SASL/IAM authentication is on or off for VPC connectivity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConnectivityIam) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> VpcConnectivityIam:
    out: VpcConnectivityIam = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
