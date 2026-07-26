"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#StartInstanceOnboardingJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.instance_onboarding_job_status


class StartInstanceOnboardingJobResponse(TypedDict, closed=True):
    connect_instance_onboarding_job_status: NotRequired[
        "capo_connectcampaignsv2.types.instance_onboarding_job_status.InstanceOnboardingJobStatus"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: StartInstanceOnboardingJobResponse) -> dict:
    out: dict = {}
    if "connect_instance_onboarding_job_status" in value:
        import capo_connectcampaignsv2.types.instance_onboarding_job_status

        out["connectInstanceOnboardingJobStatus"] = (
            capo_connectcampaignsv2.types.instance_onboarding_job_status.serialize_json(
                value["connect_instance_onboarding_job_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartInstanceOnboardingJobResponse:
    out: StartInstanceOnboardingJobResponse = {}  # type: ignore[typeddict-item]
    if "connectInstanceOnboardingJobStatus" in data:
        import capo_connectcampaignsv2.types.instance_onboarding_job_status

        out["connect_instance_onboarding_job_status"] = (
            capo_connectcampaignsv2.types.instance_onboarding_job_status.deserialize_json(
                data["connectInstanceOnboardingJobStatus"]
            )
        )
    return out
