"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorLocalResource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.monitor_local_resource_type


class MonitorLocalResource(TypedDict):
    type: "aws_sdk_networkflowmonitor.types.monitor_local_resource_type.MonitorLocalResourceType"
    """<p>The type of the local resource. Valid values are <code>AWS::EC2::VPC</code> <code>AWS::AvailabilityZone</code>, <code>AWS::EC2::Subnet</code>, <code>AWS::EKS::Cluster</code>, or <code>AWS::Region</code>.</p>"""
    identifier: "str"
    """<p>The identifier of the local resource. The values you can specify are the following:</p> <ul> <li> <p>For a VPC, subnet or EKS cluster, this identifier is the VPC Amazon Resource Name (ARN), subnet ARN or cluster ARN.</p> </li> <li> <p>For an Availability Zone, this identifier is the AZ name, for example, us-west-2b.</p> </li> <li> <p>For a Region, this identifier is the Region name, for example, us-west-2.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitorLocalResource) -> dict:
    out: dict = {}
    import aws_sdk_networkflowmonitor.types.monitor_local_resource_type

    out["type"] = (
        aws_sdk_networkflowmonitor.types.monitor_local_resource_type.serialize_json(
            value["type"]
        )
    )
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> MonitorLocalResource:
    out: MonitorLocalResource = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_networkflowmonitor.types.monitor_local_resource_type

        out["type"] = (
            aws_sdk_networkflowmonitor.types.monitor_local_resource_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("MonitorLocalResource.type required")
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("MonitorLocalResource.identifier required")
    return out
