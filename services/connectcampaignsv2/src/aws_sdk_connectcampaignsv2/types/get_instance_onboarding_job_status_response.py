"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#GetInstanceOnboardingJobStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.instance_onboarding_job_status


class GetInstanceOnboardingJobStatusResponse(TypedDict, closed=True):
    connect_instance_onboarding_job_status: NotRequired[
        "aws_sdk_connectcampaignsv2.types.instance_onboarding_job_status.InstanceOnboardingJobStatus"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetInstanceOnboardingJobStatusResponse) -> dict:
    out: dict = {}
    if "connect_instance_onboarding_job_status" in value:
        import aws_sdk_connectcampaignsv2.types.instance_onboarding_job_status

        out["connectInstanceOnboardingJobStatus"] = (
            aws_sdk_connectcampaignsv2.types.instance_onboarding_job_status.serialize_json(
                value["connect_instance_onboarding_job_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetInstanceOnboardingJobStatusResponse:
    out: GetInstanceOnboardingJobStatusResponse = {}  # type: ignore[typeddict-item]
    if "connectInstanceOnboardingJobStatus" in data:
        import aws_sdk_connectcampaignsv2.types.instance_onboarding_job_status

        out["connect_instance_onboarding_job_status"] = (
            aws_sdk_connectcampaignsv2.types.instance_onboarding_job_status.deserialize_json(
                data["connectInstanceOnboardingJobStatus"]
            )
        )
    return out
