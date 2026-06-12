"""Generated from Smithy shape ``com.amazonaws.datasync#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datasync.types.filter_rule

FilterList: TypeAlias = list["aws_sdk_datasync.types.filter_rule.FilterRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterList) -> list:
    import aws_sdk_datasync.types.filter_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_datasync.types.filter_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FilterList:
    import aws_sdk_datasync.types.filter_rule

    out: FilterList = []
    for item in data:
        out.append(aws_sdk_datasync.types.filter_rule.deserialize_aws_json_1_1(item))
    return out
