"""Generated from Smithy shape ``com.amazonaws.sagemaker#SubscribedWorkteams``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.subscribed_workteam

SubscribedWorkteams: TypeAlias = list[
    "capo_sagemaker.types.subscribed_workteam.SubscribedWorkteam"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscribedWorkteams) -> list:
    import capo_sagemaker.types.subscribed_workteam

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.subscribed_workteam.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SubscribedWorkteams:
    import capo_sagemaker.types.subscribed_workteam

    out: SubscribedWorkteams = []
    for item in data:
        out.append(
            capo_sagemaker.types.subscribed_workteam.deserialize_aws_json_1_1(item)
        )
    return out
