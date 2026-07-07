"""Generated from Smithy shape ``com.amazonaws.dax#IncreaseReplicationFactorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dax.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dax.types.availability_zone_list
    import aws_sdk_dax.types.integer
    import aws_sdk_dax.types.string


class IncreaseReplicationFactorRequest(TypedDict, closed=True):
    cluster_name: "aws_sdk_dax.types.string.String"
    """<p>The name of the DAX cluster that will receive additional nodes.</p>"""
    new_replication_factor: "aws_sdk_dax.types.integer.Integer"
    """<p>The new number of nodes for the DAX cluster.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_dax.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>The Availability Zones (AZs) in which the cluster nodes will be created. All nodes belonging to the cluster are placed in these Availability Zones. Use this parameter if you want to distribute the nodes across multiple AZs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncreaseReplicationFactorRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    out["NewReplicationFactor"] = value.get("new_replication_factor", 0)
    if "availability_zones" in value:
        import aws_sdk_dax.types.availability_zone_list

        out["AvailabilityZones"] = (
            aws_sdk_dax.types.availability_zone_list.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IncreaseReplicationFactorRequest:
    out: IncreaseReplicationFactorRequest = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    else:
        raise DeserializationError(
            "IncreaseReplicationFactorRequest.cluster_name required"
        )
    if "NewReplicationFactor" in data:
        out["new_replication_factor"] = data["NewReplicationFactor"]
    else:
        out["new_replication_factor"] = 0
    if "AvailabilityZones" in data:
        import aws_sdk_dax.types.availability_zone_list

        out["availability_zones"] = (
            aws_sdk_dax.types.availability_zone_list.deserialize_aws_json_1_1(
                data["AvailabilityZones"]
            )
        )
    return out
