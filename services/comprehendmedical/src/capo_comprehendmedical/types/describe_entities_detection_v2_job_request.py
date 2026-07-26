"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#DescribeEntitiesDetectionV2JobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_comprehendmedical.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehendmedical.types.job_id


class DescribeEntitiesDetectionV2JobRequest(TypedDict, closed=True):
    job_id: "capo_comprehendmedical.types.job_id.JobId"
    """<p>The identifier that Amazon Comprehend Medical generated for the job. The <code>StartEntitiesDetectionV2Job</code> operation returns this identifier in its response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntitiesDetectionV2JobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntitiesDetectionV2JobRequest:
    out: DescribeEntitiesDetectionV2JobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError(
            "DescribeEntitiesDetectionV2JobRequest.job_id required"
        )
    return out
