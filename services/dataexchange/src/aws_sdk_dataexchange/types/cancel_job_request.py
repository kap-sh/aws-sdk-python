"""Generated from Smithy shape ``com.amazonaws.dataexchange#CancelJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.id


class CancelJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelJobRequest:
    out: CancelJobRequest = {}  # type: ignore[typeddict-item]
    return out
