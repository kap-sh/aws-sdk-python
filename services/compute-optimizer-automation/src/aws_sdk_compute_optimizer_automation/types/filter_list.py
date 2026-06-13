"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.filter

FilterList: TypeAlias = list["aws_sdk_compute_optimizer_automation.types.filter.Filter"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterList) -> list:
    import aws_sdk_compute_optimizer_automation.types.filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer_automation.types.filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FilterList:
    import aws_sdk_compute_optimizer_automation.types.filter

    out: FilterList = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer_automation.types.filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
