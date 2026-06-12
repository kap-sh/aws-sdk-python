"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemEventFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_event_filter

OpsItemEventFilters: TypeAlias = list[
    "aws_sdk_ssm.types.ops_item_event_filter.OpsItemEventFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemEventFilters) -> list:
    import aws_sdk_ssm.types.ops_item_event_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.ops_item_event_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsItemEventFilters:
    import aws_sdk_ssm.types.ops_item_event_filter

    out: OpsItemEventFilters = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.ops_item_event_filter.deserialize_aws_json_1_1(item)
        )
    return out
