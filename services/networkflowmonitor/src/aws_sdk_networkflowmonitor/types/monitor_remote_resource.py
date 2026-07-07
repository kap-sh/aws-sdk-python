"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorRemoteResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.monitor_remote_resource_type


class MonitorRemoteResource(TypedDict, closed=True):
    type: "aws_sdk_networkflowmonitor.types.monitor_remote_resource_type.MonitorRemoteResourceType"
    """<p>The type of the remote resource. Valid values are <code>AWS::EC2::VPC</code> <code>AWS::AvailabilityZone</code>, <code>AWS::EC2::Subnet</code>, <code>AWS::AWSService</code>, or <code>AWS::Region</code>.</p>"""
    identifier: "str"
    """<p>The identifier of the remote resource. For a VPC or subnet, this identifier is the VPC Amazon Resource Name (ARN) or subnet ARN. For an Availability Zone, this identifier is the AZ name, for example, us-west-2b. For an Amazon Web Services Region , this identifier is the Region name, for example, us-west-2. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitorRemoteResource) -> dict:
    out: dict = {}
    import aws_sdk_networkflowmonitor.types.monitor_remote_resource_type

    out["type"] = (
        aws_sdk_networkflowmonitor.types.monitor_remote_resource_type.serialize_json(
            value["type"]
        )
    )
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> MonitorRemoteResource:
    out: MonitorRemoteResource = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_networkflowmonitor.types.monitor_remote_resource_type

        out["type"] = (
            aws_sdk_networkflowmonitor.types.monitor_remote_resource_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("MonitorRemoteResource.type required")
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("MonitorRemoteResource.identifier required")
    return out
