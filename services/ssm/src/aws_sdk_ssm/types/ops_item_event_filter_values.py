"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemEventFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_event_filter_value

OpsItemEventFilterValues: TypeAlias = list[
    "aws_sdk_ssm.types.ops_item_event_filter_value.OpsItemEventFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemEventFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OpsItemEventFilterValues:
    return list(data)
