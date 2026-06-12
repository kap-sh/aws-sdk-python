"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ParameterMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.parameter_mapping

ParameterMappingList: TypeAlias = list[
    "aws_sdk_timestream_query.types.parameter_mapping.ParameterMapping"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ParameterMappingList) -> list:
    import aws_sdk_timestream_query.types.parameter_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_timestream_query.types.parameter_mapping.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ParameterMappingList:
    import aws_sdk_timestream_query.types.parameter_mapping

    out: ParameterMappingList = []
    for item in data:
        out.append(
            aws_sdk_timestream_query.types.parameter_mapping.deserialize_aws_json_1_0(
                item
            )
        )
    return out
