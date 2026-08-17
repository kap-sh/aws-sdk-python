"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.parameter_string_filter

ParameterStringFilterList: TypeAlias = list[
    "capo_ssm.types.parameter_string_filter.ParameterStringFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterStringFilterList) -> list:
    import capo_ssm.types.parameter_string_filter

    out: list = []
    for item in value:
        out.append(capo_ssm.types.parameter_string_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterStringFilterList:
    import capo_ssm.types.parameter_string_filter

    out: ParameterStringFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.parameter_string_filter.deserialize_aws_json_1_1(item)
        )
    return out
