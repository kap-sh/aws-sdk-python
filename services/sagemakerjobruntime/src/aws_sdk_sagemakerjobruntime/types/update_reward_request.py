"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#UpdateRewardRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemakerjobruntime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemakerjobruntime.types.double_list
    import aws_sdk_sagemakerjobruntime.types.job_arn
    import aws_sdk_sagemakerjobruntime.types.trajectory_id


class UpdateRewardRequest(TypedDict):
    job_arn: "aws_sdk_sagemakerjobruntime.types.job_arn.JobArn"
    """The job ARN."""
    trajectory_id: "aws_sdk_sagemakerjobruntime.types.trajectory_id.TrajectoryId"
    """The trajectory ID to update with reward values."""
    rewards: "aws_sdk_sagemakerjobruntime.types.double_list.DoubleList"
    """The list of reward values to assign to this trajectory. Provide one reward value per turn in the trajectory."""
    client_token: NotRequired["str"]
    """A unique, case-sensitive identifier that you provide to ensure the idempotency of the request."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRewardRequest) -> dict:
    out: dict = {}
    out["TrajectoryId"] = value["trajectory_id"]
    import aws_sdk_sagemakerjobruntime.types.double_list

    out["Rewards"] = aws_sdk_sagemakerjobruntime.types.double_list.serialize_json(
        value["rewards"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateRewardRequest:
    out: UpdateRewardRequest = {}  # type: ignore[typeddict-item]
    if "TrajectoryId" in data:
        out["trajectory_id"] = data["TrajectoryId"]
    else:
        raise DeserializationError("UpdateRewardRequest.trajectory_id required")
    if "Rewards" in data:
        import aws_sdk_sagemakerjobruntime.types.double_list

        out["rewards"] = aws_sdk_sagemakerjobruntime.types.double_list.deserialize_json(
            data["Rewards"]
        )
    else:
        raise DeserializationError("UpdateRewardRequest.rewards required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
