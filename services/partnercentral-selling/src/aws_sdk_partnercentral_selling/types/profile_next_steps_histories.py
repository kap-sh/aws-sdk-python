"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProfileNextStepsHistories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.profile_next_steps_history

ProfileNextStepsHistories: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.profile_next_steps_history.ProfileNextStepsHistory"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProfileNextStepsHistories) -> list:
    import aws_sdk_partnercentral_selling.types.profile_next_steps_history

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.profile_next_steps_history.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProfileNextStepsHistories:
    import aws_sdk_partnercentral_selling.types.profile_next_steps_history

    out: ProfileNextStepsHistories = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.profile_next_steps_history.deserialize_aws_json_1_0(
                item
            )
        )
    return out
