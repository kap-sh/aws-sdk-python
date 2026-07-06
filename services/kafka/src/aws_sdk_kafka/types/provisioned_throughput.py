"""Generated from Smithy shape ``com.amazonaws.kafka#ProvisionedThroughput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean
    import aws_sdk_kafka.types.__integer


class ProvisionedThroughput(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>Provisioned throughput is enabled or not.</p>"""
    volume_throughput: NotRequired["aws_sdk_kafka.types.__integer.__integer"]
    """<p>Throughput value of the EBS volumes for the data drive on each kafka broker node in MiB per second.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedThroughput) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "volume_throughput" in value:
        out["volumeThroughput"] = value["volume_throughput"]
    return out


def deserialize_json(data: dict) -> ProvisionedThroughput:
    out: ProvisionedThroughput = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "volumeThroughput" in data:
        out["volume_throughput"] = data["volumeThroughput"]
    return out
