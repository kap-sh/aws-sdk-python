"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ReplicationSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.region_info_map
    import aws_sdk_ssm_incidents.types.replication_set_status


class ReplicationSet(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_ssm_incidents.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the replication set.</p>"""
    region_map: "aws_sdk_ssm_incidents.types.region_info_map.RegionInfoMap"
    """<p>The map between each Amazon Web Services Region in your replication set and the KMS key that's used to encrypt the data in that Region.</p>"""
    status: "aws_sdk_ssm_incidents.types.replication_set_status.ReplicationSetStatus"
    """<p>The status of the replication set. If the replication set is still pending, you can't use Incident Manager functionality.</p>"""
    deletion_protected: "bool"
    """<p>Determines if the replication set deletion protection is enabled or not. If deletion protection is enabled, you can't delete the last Amazon Web Services Region in the replication set. </p>"""
    created_time: "datetime.datetime"
    """<p>When the replication set was created.</p>"""
    created_by: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>Details about who created the replication set.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>When the replication set was last updated.</p>"""
    last_modified_by: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>Who last modified the replication set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationSet) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    import aws_sdk_ssm_incidents.types.region_info_map

    out["regionMap"] = aws_sdk_ssm_incidents.types.region_info_map.serialize_json(
        value["region_map"]
    )
    out["status"] = value["status"]
    out["deletionProtected"] = value["deletion_protected"]
    import aws_sdk_ssm_incidents.types._prelude.timestamp

    out["createdTime"] = aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["created_time"]
    )
    out["createdBy"] = value["created_by"]
    import aws_sdk_ssm_incidents.types._prelude.timestamp

    out["lastModifiedTime"] = (
        aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["last_modified_time"]
        )
    )
    out["lastModifiedBy"] = value["last_modified_by"]
    return out


def deserialize_json(data: dict) -> ReplicationSet:
    out: ReplicationSet = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "regionMap" in data:
        import aws_sdk_ssm_incidents.types.region_info_map

        out["region_map"] = (
            aws_sdk_ssm_incidents.types.region_info_map.deserialize_json(
                data["regionMap"]
            )
        )
    else:
        raise DeserializationError("ReplicationSet.region_map required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ReplicationSet.status required")
    if "deletionProtected" in data:
        out["deletion_protected"] = data["deletionProtected"]
    else:
        raise DeserializationError("ReplicationSet.deletion_protected required")
    if "createdTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["created_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        raise DeserializationError("ReplicationSet.created_time required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("ReplicationSet.created_by required")
    if "lastModifiedTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("ReplicationSet.last_modified_time required")
    if "lastModifiedBy" in data:
        out["last_modified_by"] = data["lastModifiedBy"]
    else:
        raise DeserializationError("ReplicationSet.last_modified_by required")
    return out
