"""Generated from Smithy shape ``com.amazonaws.emr#GetOnClusterAppUIPresignedURLInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.arn_type
    import aws_sdk_emr.types.boolean_object
    import aws_sdk_emr.types.on_cluster_app_ui_type
    import aws_sdk_emr.types.xml_string_max_len256


class GetOnClusterAppUIPresignedURLInput(TypedDict, closed=True):
    cluster_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The cluster ID associated with the cluster's application user interface presigned URL.</p>"""
    on_cluster_app_ui_type: NotRequired[
        "aws_sdk_emr.types.on_cluster_app_ui_type.OnClusterAppUIType"
    ]
    """<p>The application UI type associated with the cluster's application user interface presigned URL.</p>"""
    application_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The application ID associated with the cluster's application user interface presigned URL.</p>"""
    dry_run: NotRequired["aws_sdk_emr.types.boolean_object.BooleanObject"]
    """<p>Determines if the user interface presigned URL is for a dry run.</p>"""
    execution_role_arn: NotRequired["aws_sdk_emr.types.arn_type.ArnType"]
    """<p>The execution role ARN associated with the cluster's application user interface presigned URL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOnClusterAppUIPresignedURLInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "on_cluster_app_ui_type" in value:
        import aws_sdk_emr.types.on_cluster_app_ui_type

        out["OnClusterAppUIType"] = (
            aws_sdk_emr.types.on_cluster_app_ui_type.serialize_aws_json_1_1(
                value["on_cluster_app_ui_type"]
            )
        )
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOnClusterAppUIPresignedURLInput:
    out: GetOnClusterAppUIPresignedURLInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "OnClusterAppUIType" in data:
        import aws_sdk_emr.types.on_cluster_app_ui_type

        out["on_cluster_app_ui_type"] = (
            aws_sdk_emr.types.on_cluster_app_ui_type.deserialize_aws_json_1_1(
                data["OnClusterAppUIType"]
            )
        )
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    return out
