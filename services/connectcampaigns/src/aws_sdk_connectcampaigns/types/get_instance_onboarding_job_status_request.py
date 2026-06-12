"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#GetInstanceOnboardingJobStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.instance_id


class GetInstanceOnboardingJobStatusRequest(TypedDict):
    connect_instance_id: "aws_sdk_connectcampaigns.types.instance_id.InstanceId"


# --- restJson1 ser/de ---
def serialize_json(value: GetInstanceOnboardingJobStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetInstanceOnboardingJobStatusRequest:
    out: GetInstanceOnboardingJobStatusRequest = {}  # type: ignore[typeddict-item]
    return out
