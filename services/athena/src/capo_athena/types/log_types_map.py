"""Generated from Smithy shape ``com.amazonaws.athena#LogTypesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.log_type_key
    import capo_athena.types.log_type_values_list

LogTypesMap: TypeAlias = dict[
    "capo_athena.types.log_type_key.LogTypeKey",
    "capo_athena.types.log_type_values_list.LogTypeValuesList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LogTypesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_athena.types.log_type_values_list

        out[key] = capo_athena.types.log_type_values_list.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> LogTypesMap:
    out: LogTypesMap = {}
    for key, value in data.items():
        import capo_athena.types.log_type_values_list

        out[key] = capo_athena.types.log_type_values_list.deserialize_aws_json_1_1(
            value
        )
    return out
