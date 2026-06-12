"""Generated from Smithy shape ``com.amazonaws.codepipeline#ThirdPartyJobDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.nonce
    import aws_sdk_codepipeline.types.third_party_job_data
    import aws_sdk_codepipeline.types.third_party_job_id


class ThirdPartyJobDetails(TypedDict):
    id: NotRequired["aws_sdk_codepipeline.types.third_party_job_id.ThirdPartyJobId"]
    """<p>The identifier used to identify the job details in CodePipeline.</p>"""
    data: NotRequired[
        "aws_sdk_codepipeline.types.third_party_job_data.ThirdPartyJobData"
    ]
    """<p>The data to be returned by the third party job worker.</p>"""
    nonce: NotRequired["aws_sdk_codepipeline.types.nonce.Nonce"]
    """<p>A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Use this number in an <a>AcknowledgeThirdPartyJob</a> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThirdPartyJobDetails) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "data" in value:
        import aws_sdk_codepipeline.types.third_party_job_data

        out["data"] = (
            aws_sdk_codepipeline.types.third_party_job_data.serialize_aws_json_1_1(
                value["data"]
            )
        )
    if "nonce" in value:
        out["nonce"] = value["nonce"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThirdPartyJobDetails:
    out: ThirdPartyJobDetails = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "data" in data:
        import aws_sdk_codepipeline.types.third_party_job_data

        out["data"] = (
            aws_sdk_codepipeline.types.third_party_job_data.deserialize_aws_json_1_1(
                data["data"]
            )
        )
    if "nonce" in data:
        out["nonce"] = data["nonce"]
    return out
