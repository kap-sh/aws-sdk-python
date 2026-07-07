"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#StopApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.operation_id


class StopApplicationResponse(TypedDict, closed=True):
    operation_id: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.operation_id.OperationId"
    ]
    """<p>The operation ID that can be used to track the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopApplicationResponse) -> dict:
    out: dict = {}
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopApplicationResponse:
    out: StopApplicationResponse = {}  # type: ignore[typeddict-item]
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    return out
