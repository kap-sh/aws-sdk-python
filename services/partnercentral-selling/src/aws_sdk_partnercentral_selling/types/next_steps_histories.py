"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#NextStepsHistories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.next_steps_history

NextStepsHistories: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.next_steps_history.NextStepsHistory"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NextStepsHistories) -> list:
    import aws_sdk_partnercentral_selling.types.next_steps_history

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.next_steps_history.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NextStepsHistories:
    import aws_sdk_partnercentral_selling.types.next_steps_history

    out: NextStepsHistories = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.next_steps_history.deserialize_aws_json_1_0(
                item
            )
        )
    return out
