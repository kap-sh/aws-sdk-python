"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetThirdPartyJobDetailsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.third_party_job_details


class GetThirdPartyJobDetailsOutput(TypedDict, closed=True):
    job_details: NotRequired[
        "capo_codepipeline.types.third_party_job_details.ThirdPartyJobDetails"
    ]
    """<p>The details of the job, including any protected values defined for the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetThirdPartyJobDetailsOutput) -> dict:
    out: dict = {}
    if "job_details" in value:
        import capo_codepipeline.types.third_party_job_details

        out["jobDetails"] = (
            capo_codepipeline.types.third_party_job_details.serialize_aws_json_1_1(
                value["job_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetThirdPartyJobDetailsOutput:
    out: GetThirdPartyJobDetailsOutput = {}  # type: ignore[typeddict-item]
    if "jobDetails" in data:
        import capo_codepipeline.types.third_party_job_details

        out["job_details"] = (
            capo_codepipeline.types.third_party_job_details.deserialize_aws_json_1_1(
                data["jobDetails"]
            )
        )
    return out
