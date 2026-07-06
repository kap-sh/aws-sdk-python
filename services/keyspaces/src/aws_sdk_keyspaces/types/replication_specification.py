"""Generated from Smithy shape ``com.amazonaws.keyspaces#ReplicationSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.region_list
    import aws_sdk_keyspaces.types.rs


class ReplicationSpecification(TypedDict, closed=True):
    replication_strategy: "aws_sdk_keyspaces.types.rs.rs"
    """<p> The <code>replicationStrategy</code> of a keyspace, the required value is <code>SINGLE_REGION</code> or <code>MULTI_REGION</code>. </p>"""
    region_list: NotRequired["aws_sdk_keyspaces.types.region_list.RegionList"]
    """<p> The <code>regionList</code> contains the Amazon Web Services Regions where the keyspace is replicated in. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicationSpecification) -> dict:
    out: dict = {}
    out["replicationStrategy"] = value["replication_strategy"]
    if "region_list" in value:
        import aws_sdk_keyspaces.types.region_list

        out["regionList"] = aws_sdk_keyspaces.types.region_list.serialize_aws_json_1_0(
            value["region_list"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicationSpecification:
    out: ReplicationSpecification = {}  # type: ignore[typeddict-item]
    if "replicationStrategy" in data:
        out["replication_strategy"] = data["replicationStrategy"]
    else:
        raise DeserializationError(
            "ReplicationSpecification.replication_strategy required"
        )
    if "regionList" in data:
        import aws_sdk_keyspaces.types.region_list

        out["region_list"] = (
            aws_sdk_keyspaces.types.region_list.deserialize_aws_json_1_0(
                data["regionList"]
            )
        )
    return out
