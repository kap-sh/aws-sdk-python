"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemEventFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_event_filter

OpsItemEventFilters: TypeAlias = list[
    "capo_ssm.types.ops_item_event_filter.OpsItemEventFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemEventFilters) -> list:
    import capo_ssm.types.ops_item_event_filter

    out: list = []
    for item in value:
        out.append(capo_ssm.types.ops_item_event_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsItemEventFilters:
    import capo_ssm.types.ops_item_event_filter

    out: OpsItemEventFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.ops_item_event_filter.deserialize_aws_json_1_1(item))
    return out
