"""Generated from Smithy shape ``com.amazonaws.textract#HumanLoopActivationReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.human_loop_activation_reason

HumanLoopActivationReasons: TypeAlias = list[
    "capo_textract.types.human_loop_activation_reason.HumanLoopActivationReason"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanLoopActivationReasons) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> HumanLoopActivationReasons:
    return list(data)
