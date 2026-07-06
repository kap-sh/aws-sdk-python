"""Generated from Smithy shape ``com.amazonaws.drs#GetFailbackReplicationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.bounded_string
    import aws_sdk_drs.types.internet_protocol
    import aws_sdk_drs.types.positive_integer
    import aws_sdk_drs.types.recovery_instance_id


class GetFailbackReplicationConfigurationResponse(TypedDict, closed=True):
    recovery_instance_id: "aws_sdk_drs.types.recovery_instance_id.RecoveryInstanceID"
    """<p>The ID of the Recovery Instance.</p>"""
    name: NotRequired["aws_sdk_drs.types.bounded_string.BoundedString"]
    """<p>The name of the Failback Replication Configuration.</p>"""
    bandwidth_throttling: "aws_sdk_drs.types.positive_integer.PositiveInteger"
    """<p>Configure bandwidth throttling for the outbound data transfer rate of the Recovery Instance in Mbps.</p>"""
    use_private_ip: NotRequired["bool"]
    """<p>Whether to use Private IP for the failback replication of the Recovery Instance.</p>"""
    internet_protocol: NotRequired[
        "aws_sdk_drs.types.internet_protocol.InternetProtocol"
    ]
    """<p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFailbackReplicationConfigurationResponse) -> dict:
    out: dict = {}
    out["recoveryInstanceID"] = value["recovery_instance_id"]
    if "name" in value:
        out["name"] = value["name"]
    out["bandwidthThrottling"] = value.get("bandwidth_throttling", 0)
    if "use_private_ip" in value:
        out["usePrivateIP"] = value["use_private_ip"]
    if "internet_protocol" in value:
        out["internetProtocol"] = value["internet_protocol"]
    return out


def deserialize_json(data: dict) -> GetFailbackReplicationConfigurationResponse:
    out: GetFailbackReplicationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "recoveryInstanceID" in data:
        out["recovery_instance_id"] = data["recoveryInstanceID"]
    else:
        raise DeserializationError(
            "GetFailbackReplicationConfigurationResponse.recovery_instance_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    if "bandwidthThrottling" in data:
        out["bandwidth_throttling"] = data["bandwidthThrottling"]
    else:
        out["bandwidth_throttling"] = 0
    if "usePrivateIP" in data:
        out["use_private_ip"] = data["usePrivateIP"]
    if "internetProtocol" in data:
        out["internet_protocol"] = data["internetProtocol"]
    return out
