"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#UpdateApplicationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_detail
    import aws_sdk_kinesis_analytics_v2.types.operation_id


class UpdateApplicationResponse(TypedDict):
    application_detail: (
        "aws_sdk_kinesis_analytics_v2.types.application_detail.ApplicationDetail"
    )
    """<p>Describes application updates.</p>"""
    operation_id: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.operation_id.OperationId"
    ]
    """<p>The operation ID that can be used to track the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationResponse) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.application_detail

    out["ApplicationDetail"] = (
        aws_sdk_kinesis_analytics_v2.types.application_detail.serialize_aws_json_1_1(
            value["application_detail"]
        )
    )
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationResponse:
    out: UpdateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationDetail" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_detail

        out["application_detail"] = (
            aws_sdk_kinesis_analytics_v2.types.application_detail.deserialize_aws_json_1_1(
                data["ApplicationDetail"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateApplicationResponse.application_detail required"
        )
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    return out
