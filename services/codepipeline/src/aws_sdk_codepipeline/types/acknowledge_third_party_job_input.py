"""Generated from Smithy shape ``com.amazonaws.codepipeline#AcknowledgeThirdPartyJobInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.client_token
    import aws_sdk_codepipeline.types.nonce
    import aws_sdk_codepipeline.types.third_party_job_id


class AcknowledgeThirdPartyJobInput(TypedDict):
    job_id: "aws_sdk_codepipeline.types.third_party_job_id.ThirdPartyJobId"
    """<p>The unique system-generated ID of the job.</p>"""
    nonce: "aws_sdk_codepipeline.types.nonce.Nonce"
    """<p>A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response to a <a>GetThirdPartyJobDetails</a> request.</p>"""
    client_token: "aws_sdk_codepipeline.types.client_token.ClientToken"
    """<p>The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcknowledgeThirdPartyJobInput) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["nonce"] = value["nonce"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AcknowledgeThirdPartyJobInput:
    out: AcknowledgeThirdPartyJobInput = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("AcknowledgeThirdPartyJobInput.job_id required")
    if "nonce" in data:
        out["nonce"] = data["nonce"]
    else:
        raise DeserializationError("AcknowledgeThirdPartyJobInput.nonce required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "AcknowledgeThirdPartyJobInput.client_token required"
        )
    return out
