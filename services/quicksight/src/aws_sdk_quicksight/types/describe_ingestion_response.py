"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeIngestionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.ingestion
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeIngestionResponse(TypedDict):
    ingestion: NotRequired["aws_sdk_quicksight.types.ingestion.Ingestion"]
    """<p>Information about the ingestion.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIngestionResponse) -> dict:
    out: dict = {}
    if "ingestion" in value:
        import aws_sdk_quicksight.types.ingestion

        out["Ingestion"] = aws_sdk_quicksight.types.ingestion.serialize_json(
            value["ingestion"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeIngestionResponse:
    out: DescribeIngestionResponse = {}  # type: ignore[typeddict-item]
    if "Ingestion" in data:
        import aws_sdk_quicksight.types.ingestion

        out["ingestion"] = aws_sdk_quicksight.types.ingestion.deserialize_json(
            data["Ingestion"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
