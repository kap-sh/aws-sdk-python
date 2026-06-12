"""Generated from Smithy shape ``com.amazonaws.athena#LogTypesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.log_type_key
    import aws_sdk_athena.types.log_type_values_list

LogTypesMap: TypeAlias = dict[
    "aws_sdk_athena.types.log_type_key.LogTypeKey",
    "aws_sdk_athena.types.log_type_values_list.LogTypeValuesList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LogTypesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_athena.types.log_type_values_list

        out[key] = aws_sdk_athena.types.log_type_values_list.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogTypesMap:
    out: LogTypesMap = {}
    for key, value in data.items():
        import aws_sdk_athena.types.log_type_values_list

        out[key] = aws_sdk_athena.types.log_type_values_list.deserialize_aws_json_1_1(
            value
        )
    return out
