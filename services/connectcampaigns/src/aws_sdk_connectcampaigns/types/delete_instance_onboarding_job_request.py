"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#DeleteInstanceOnboardingJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.instance_id


class DeleteInstanceOnboardingJobRequest(TypedDict, closed=True):
    connect_instance_id: "aws_sdk_connectcampaigns.types.instance_id.InstanceId"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInstanceOnboardingJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInstanceOnboardingJobRequest:
    out: DeleteInstanceOnboardingJobRequest = {}  # type: ignore[typeddict-item]
    return out
