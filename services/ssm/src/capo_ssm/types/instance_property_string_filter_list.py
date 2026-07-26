"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePropertyStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.instance_property_string_filter

InstancePropertyStringFilterList: TypeAlias = list[
    "capo_ssm.types.instance_property_string_filter.InstancePropertyStringFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePropertyStringFilterList) -> list:
    import capo_ssm.types.instance_property_string_filter

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.instance_property_string_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstancePropertyStringFilterList:
    import capo_ssm.types.instance_property_string_filter

    out: InstancePropertyStringFilterList = []
    for item in data:
        out.append(
            capo_ssm.types.instance_property_string_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
