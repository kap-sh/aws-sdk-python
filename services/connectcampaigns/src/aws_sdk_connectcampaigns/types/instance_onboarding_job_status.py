"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#InstanceOnboardingJobStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.instance_id
    import aws_sdk_connectcampaigns.types.instance_onboarding_job_failure_code
    import aws_sdk_connectcampaigns.types.instance_onboarding_job_status_code


class InstanceOnboardingJobStatus(TypedDict):
    connect_instance_id: "aws_sdk_connectcampaigns.types.instance_id.InstanceId"
    status: "aws_sdk_connectcampaigns.types.instance_onboarding_job_status_code.InstanceOnboardingJobStatusCode"
    failure_code: NotRequired[
        "aws_sdk_connectcampaigns.types.instance_onboarding_job_failure_code.InstanceOnboardingJobFailureCode"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceOnboardingJobStatus) -> dict:
    out: dict = {}
    out["connectInstanceId"] = value["connect_instance_id"]
    out["status"] = value["status"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    return out


def deserialize_json(data: dict) -> InstanceOnboardingJobStatus:
    out: InstanceOnboardingJobStatus = {}  # type: ignore[typeddict-item]
    if "connectInstanceId" in data:
        out["connect_instance_id"] = data["connectInstanceId"]
    else:
        raise DeserializationError(
            "InstanceOnboardingJobStatus.connect_instance_id required"
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("InstanceOnboardingJobStatus.status required")
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    return out
