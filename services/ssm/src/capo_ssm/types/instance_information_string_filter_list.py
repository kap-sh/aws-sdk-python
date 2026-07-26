"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceInformationStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.instance_information_string_filter

InstanceInformationStringFilterList: TypeAlias = list[
    "capo_ssm.types.instance_information_string_filter.InstanceInformationStringFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInformationStringFilterList) -> list:
    import capo_ssm.types.instance_information_string_filter

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.instance_information_string_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceInformationStringFilterList:
    import capo_ssm.types.instance_information_string_filter

    out: InstanceInformationStringFilterList = []
    for item in data:
        out.append(
            capo_ssm.types.instance_information_string_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
