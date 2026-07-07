"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RdsCreateCrossRegionReplicaConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.iam_role_arn
    import aws_sdk_arc_region_switch.types.rds_db_instance_arn_map


class RdsCreateCrossRegionReplicaConfiguration(TypedDict, closed=True):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    cross_account_role: NotRequired[
        "aws_sdk_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross-account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    db_instance_arn_map: (
        "aws_sdk_arc_region_switch.types.rds_db_instance_arn_map.RdsDbInstanceArnMap"
    )
    """<p>A map of database instance ARNs for each Region in the plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RdsCreateCrossRegionReplicaConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    import aws_sdk_arc_region_switch.types.rds_db_instance_arn_map

    out["dbInstanceArnMap"] = (
        aws_sdk_arc_region_switch.types.rds_db_instance_arn_map.serialize_aws_json_1_0(
            value["db_instance_arn_map"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RdsCreateCrossRegionReplicaConfiguration:
    out: RdsCreateCrossRegionReplicaConfiguration = {}  # type: ignore[typeddict-item]
    if "timeoutMinutes" in data:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if "crossAccountRole" in data:
        out["cross_account_role"] = data["crossAccountRole"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "dbInstanceArnMap" in data:
        import aws_sdk_arc_region_switch.types.rds_db_instance_arn_map

        out["db_instance_arn_map"] = (
            aws_sdk_arc_region_switch.types.rds_db_instance_arn_map.deserialize_aws_json_1_0(
                data["dbInstanceArnMap"]
            )
        )
    else:
        raise DeserializationError(
            "RdsCreateCrossRegionReplicaConfiguration.db_instance_arn_map required"
        )
    return out
