"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#DescribeRxNormInferenceJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_comprehendmedical.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehendmedical.types.job_id


class DescribeRxNormInferenceJobRequest(TypedDict, closed=True):
    job_id: "capo_comprehendmedical.types.job_id.JobId"
    """<p>The identifier that Amazon Comprehend Medical generated for the job. The StartRxNormInferenceJob operation returns this identifier in its response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRxNormInferenceJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRxNormInferenceJobRequest:
    out: DescribeRxNormInferenceJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("DescribeRxNormInferenceJobRequest.job_id required")
    return out
