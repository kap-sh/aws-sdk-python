"""Generated from Smithy shape ``com.amazonaws.signer#DescribeSigningJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_signer.types.job_id


class DescribeSigningJobRequest(TypedDict, closed=True):
    job_id: "aws_sdk_signer.types.job_id.JobId"
    """<p>The ID of the signing job on input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSigningJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSigningJobRequest:
    out: DescribeSigningJobRequest = {}  # type: ignore[typeddict-item]
    return out
