"""Generated from Smithy shape ``com.amazonaws.dataexchange#GetJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.id


class GetJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetJobRequest:
    out: GetJobRequest = {}  # type: ignore[typeddict-item]
    return out
