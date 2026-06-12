"""Generated from Smithy shape ``com.amazonaws.voiceid#DescribeFraudsterRegistrationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.job_id


class DescribeFraudsterRegistrationJobRequest(TypedDict):
    domain_id: "aws_sdk_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the fraudster registration job.</p>"""
    job_id: "aws_sdk_voice_id.types.job_id.JobId"
    """<p>The identifier of the fraudster registration job you are describing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFraudsterRegistrationJobRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFraudsterRegistrationJobRequest:
    out: DescribeFraudsterRegistrationJobRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError(
            "DescribeFraudsterRegistrationJobRequest.domain_id required"
        )
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError(
            "DescribeFraudsterRegistrationJobRequest.job_id required"
        )
    return out
