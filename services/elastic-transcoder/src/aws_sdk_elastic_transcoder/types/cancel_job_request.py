"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CancelJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.id


class CancelJobRequest(TypedDict, closed=True):
    id: "aws_sdk_elastic_transcoder.types.id.Id"
    """<p>The identifier of the job that you want to cancel.</p> <p>To get a list of the jobs (including their <code>jobId</code>) that have a status of <code>Submitted</code>, use the <a>ListJobsByStatus</a> API action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelJobRequest:
    out: CancelJobRequest = {}  # type: ignore[typeddict-item]
    return out
