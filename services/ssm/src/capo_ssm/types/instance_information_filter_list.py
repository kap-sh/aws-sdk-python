"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceInformationFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.instance_information_filter

InstanceInformationFilterList: TypeAlias = list[
    "capo_ssm.types.instance_information_filter.InstanceInformationFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInformationFilterList) -> list:
    import capo_ssm.types.instance_information_filter

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.instance_information_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceInformationFilterList:
    import capo_ssm.types.instance_information_filter

    out: InstanceInformationFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.instance_information_filter.deserialize_aws_json_1_1(item)
        )
    return out
