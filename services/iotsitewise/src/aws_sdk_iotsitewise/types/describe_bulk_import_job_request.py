"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeBulkImportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class DescribeBulkImportJobRequest(TypedDict):
    job_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBulkImportJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBulkImportJobRequest:
    out: DescribeBulkImportJobRequest = {}  # type: ignore[typeddict-item]
    return out
