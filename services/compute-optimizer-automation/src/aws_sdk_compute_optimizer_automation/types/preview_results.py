"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#PreviewResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.preview_result

PreviewResults: TypeAlias = list[
    "aws_sdk_compute_optimizer_automation.types.preview_result.PreviewResult"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreviewResults) -> list:
    import aws_sdk_compute_optimizer_automation.types.preview_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer_automation.types.preview_result.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PreviewResults:
    import aws_sdk_compute_optimizer_automation.types.preview_result

    out: PreviewResults = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer_automation.types.preview_result.deserialize_aws_json_1_0(
                item
            )
        )
    return out
