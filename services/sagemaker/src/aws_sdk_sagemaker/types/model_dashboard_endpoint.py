"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelDashboardEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_arn
    import aws_sdk_sagemaker.types.endpoint_name
    import aws_sdk_sagemaker.types.endpoint_status
    import aws_sdk_sagemaker.types.timestamp


class ModelDashboardEndpoint(TypedDict, closed=True):
    endpoint_name: NotRequired["aws_sdk_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The endpoint name.</p>"""
    endpoint_arn: NotRequired["aws_sdk_sagemaker.types.endpoint_arn.EndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the endpoint.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the endpoint was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The last time the endpoint was modified.</p>"""
    endpoint_status: NotRequired[
        "aws_sdk_sagemaker.types.endpoint_status.EndpointStatus"
    ]
    """<p>The endpoint status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelDashboardEndpoint) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
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
    if "endpoint_status" in value:
        import aws_sdk_sagemaker.types.endpoint_status

        out["EndpointStatus"] = (
            aws_sdk_sagemaker.types.endpoint_status.serialize_aws_json_1_1(
                value["endpoint_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelDashboardEndpoint:
    out: ModelDashboardEndpoint = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
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
    if "EndpointStatus" in data:
        import aws_sdk_sagemaker.types.endpoint_status

        out["endpoint_status"] = (
            aws_sdk_sagemaker.types.endpoint_status.deserialize_aws_json_1_1(
                data["EndpointStatus"]
            )
        )
    return out
