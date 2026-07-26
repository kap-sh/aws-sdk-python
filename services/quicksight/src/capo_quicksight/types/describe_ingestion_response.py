"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeIngestionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.ingestion
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeIngestionResponse(TypedDict, closed=True):
    ingestion: NotRequired["capo_quicksight.types.ingestion.Ingestion"]
    """<p>Information about the ingestion.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIngestionResponse) -> dict:
    out: dict = {}
    if "ingestion" in value:
        import capo_quicksight.types.ingestion

        out["Ingestion"] = capo_quicksight.types.ingestion.serialize_json(
            value["ingestion"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeIngestionResponse:
    out: DescribeIngestionResponse = {}  # type: ignore[typeddict-item]
    if "Ingestion" in data:
        import capo_quicksight.types.ingestion

        out["ingestion"] = capo_quicksight.types.ingestion.deserialize_json(
            data["Ingestion"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
