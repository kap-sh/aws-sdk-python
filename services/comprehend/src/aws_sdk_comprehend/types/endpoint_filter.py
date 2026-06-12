"""Generated from Smithy shape ``com.amazonaws.comprehend#EndpointFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_model_arn
    import aws_sdk_comprehend.types.endpoint_status
    import aws_sdk_comprehend.types.timestamp


class EndpointFilter(TypedDict):
    model_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the model to which the endpoint is attached.</p>"""
    status: NotRequired["aws_sdk_comprehend.types.endpoint_status.EndpointStatus"]
    """<p>Specifies the status of the endpoint being returned. Possible values are: Creating, Ready, Updating, Deleting, Failed.</p>"""
    creation_time_before: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Specifies a date before which the returned endpoint or endpoints were created.</p>"""
    creation_time_after: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>Specifies a date after which the returned endpoint or endpoints were created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointFilter) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "status" in value:
        import aws_sdk_comprehend.types.endpoint_status

        out["Status"] = aws_sdk_comprehend.types.endpoint_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "creation_time_before" in value:
        import aws_sdk_comprehend.types.timestamp

        out["CreationTimeBefore"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "creation_time_after" in value:
        import aws_sdk_comprehend.types.timestamp

        out["CreationTimeAfter"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointFilter:
    out: EndpointFilter = {}  # type: ignore[typeddict-item]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "Status" in data:
        import aws_sdk_comprehend.types.endpoint_status

        out["status"] = (
            aws_sdk_comprehend.types.endpoint_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreationTimeBefore" in data:
        import aws_sdk_comprehend.types.timestamp

        out["creation_time_before"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "CreationTimeAfter" in data:
        import aws_sdk_comprehend.types.timestamp

        out["creation_time_after"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    return out
