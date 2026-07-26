"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_filter

OpsItemFilters: TypeAlias = list["capo_ssm.types.ops_item_filter.OpsItemFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemFilters) -> list:
    import capo_ssm.types.ops_item_filter

    out: list = []
    for item in value:
        out.append(capo_ssm.types.ops_item_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OpsItemFilters:
    import capo_ssm.types.ops_item_filter

    out: OpsItemFilters = []
    for item in data:
        out.append(capo_ssm.types.ops_item_filter.deserialize_aws_json_1_1(item))
    return out
