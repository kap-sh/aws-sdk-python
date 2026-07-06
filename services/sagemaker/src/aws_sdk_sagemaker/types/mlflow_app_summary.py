"""Generated from Smithy shape ``com.amazonaws.sagemaker#MlflowAppSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.mlflow_app_arn
    import aws_sdk_sagemaker.types.mlflow_app_name
    import aws_sdk_sagemaker.types.mlflow_app_status
    import aws_sdk_sagemaker.types.mlflow_version
    import aws_sdk_sagemaker.types.timestamp


class MlflowAppSummary(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_sagemaker.types.mlflow_app_arn.MlflowAppArn"]
    """<p>The ARN of a listed MLflow App.</p>"""
    name: NotRequired["aws_sdk_sagemaker.types.mlflow_app_name.MlflowAppName"]
    """<p>The name of the MLflow App.</p>"""
    status: NotRequired["aws_sdk_sagemaker.types.mlflow_app_status.MlflowAppStatus"]
    """<p>The status of the MLflow App.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of a listed MLflow App.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The last modified time of a listed MLflow App.</p>"""
    mlflow_version: NotRequired["aws_sdk_sagemaker.types.mlflow_version.MlflowVersion"]
    """<p>The version of a listed MLflow App.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MlflowAppSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_sagemaker.types.mlflow_app_status

        out["Status"] = (
            aws_sdk_sagemaker.types.mlflow_app_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "mlflow_version" in value:
        out["MlflowVersion"] = value["mlflow_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MlflowAppSummary:
    out: MlflowAppSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_sagemaker.types.mlflow_app_status

        out["status"] = (
            aws_sdk_sagemaker.types.mlflow_app_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "MlflowVersion" in data:
        out["mlflow_version"] = data["MlflowVersion"]
    return out
