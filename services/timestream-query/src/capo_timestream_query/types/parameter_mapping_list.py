"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ParameterMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_query.types.parameter_mapping

ParameterMappingList: TypeAlias = list[
    "capo_timestream_query.types.parameter_mapping.ParameterMapping"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ParameterMappingList) -> list:
    import capo_timestream_query.types.parameter_mapping

    out: list = []
    for item in value:
        out.append(
            capo_timestream_query.types.parameter_mapping.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ParameterMappingList:
    import capo_timestream_query.types.parameter_mapping

    out: ParameterMappingList = []
    for item in data:
        out.append(
            capo_timestream_query.types.parameter_mapping.deserialize_aws_json_1_0(item)
        )
    return out
