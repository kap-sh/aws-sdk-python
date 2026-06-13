"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RestoreFromRecoveryPointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.namespace_name
    import aws_sdk_redshift_serverless.types.workgroup_name


class RestoreFromRecoveryPointRequest(TypedDict):
    recovery_point_id: "str"
    """<p>The unique identifier of the recovery point to restore from.</p>"""
    namespace_name: "aws_sdk_redshift_serverless.types.namespace_name.NamespaceName"
    """<p>The name of the namespace to restore data into.</p>"""
    workgroup_name: "aws_sdk_redshift_serverless.types.workgroup_name.WorkgroupName"
    """<p>The name of the workgroup used to restore data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreFromRecoveryPointRequest) -> dict:
    out: dict = {}
    out["recoveryPointId"] = value["recovery_point_id"]
    out["namespaceName"] = value["namespace_name"]
    out["workgroupName"] = value["workgroup_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreFromRecoveryPointRequest:
    out: RestoreFromRecoveryPointRequest = {}  # type: ignore[typeddict-item]
    if "recoveryPointId" in data:
        out["recovery_point_id"] = data["recoveryPointId"]
    else:
        raise DeserializationError(
            "RestoreFromRecoveryPointRequest.recovery_point_id required"
        )
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    else:
        raise DeserializationError(
            "RestoreFromRecoveryPointRequest.namespace_name required"
        )
    if "workgroupName" in data:
        out["workgroup_name"] = data["workgroupName"]
    else:
        raise DeserializationError(
            "RestoreFromRecoveryPointRequest.workgroup_name required"
        )
    return out
