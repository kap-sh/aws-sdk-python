"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RecoveryPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_redshift_serverless.types.namespace_name
    import aws_sdk_redshift_serverless.types.workgroup_name


class RecoveryPoint(TypedDict, closed=True):
    recovery_point_id: NotRequired["str"]
    """<p>The unique identifier of the recovery point.</p>"""
    recovery_point_create_time: NotRequired["datetime.datetime"]
    """<p>The time the recovery point is created.</p>"""
    total_size_in_mega_bytes: NotRequired["float"]
    """<p>The total size of the data in the recovery point in megabytes.</p>"""
    namespace_name: NotRequired[
        "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the namespace the recovery point is associated with.</p>"""
    workgroup_name: NotRequired[
        "aws_sdk_redshift_serverless.types.workgroup_name.WorkgroupName"
    ]
    """<p>The name of the workgroup the recovery point is associated with.</p>"""
    namespace_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the namespace the recovery point is associated with.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecoveryPoint) -> dict:
    out: dict = {}
    if "recovery_point_id" in value:
        out["recoveryPointId"] = value["recovery_point_id"]
    if "recovery_point_create_time" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["recoveryPointCreateTime"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["recovery_point_create_time"]
            )
        )
    if "total_size_in_mega_bytes" in value:
        out["totalSizeInMegaBytes"] = value["total_size_in_mega_bytes"]
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "workgroup_name" in value:
        out["workgroupName"] = value["workgroup_name"]
    if "namespace_arn" in value:
        out["namespaceArn"] = value["namespace_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecoveryPoint:
    out: RecoveryPoint = {}  # type: ignore[typeddict-item]
    if "recoveryPointId" in data:
        out["recovery_point_id"] = data["recoveryPointId"]
    if "recoveryPointCreateTime" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["recovery_point_create_time"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["recoveryPointCreateTime"]
            )
        )
    if "totalSizeInMegaBytes" in data:
        out["total_size_in_mega_bytes"] = data["totalSizeInMegaBytes"]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    if "namespaceArn" in data:
        out["namespace_arn"] = data["namespaceArn"]
    return out
