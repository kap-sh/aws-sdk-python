"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DeleteInstanceOnboardingJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.instance_id


class DeleteInstanceOnboardingJobRequest(TypedDict):
    connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInstanceOnboardingJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInstanceOnboardingJobRequest:
    out: DeleteInstanceOnboardingJobRequest = {}  # type: ignore[typeddict-item]
    return out
