"""Generated from Smithy shape ``com.amazonaws.emr#ErrorData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.string_map

ErrorData: TypeAlias = list["aws_sdk_emr.types.string_map.StringMap"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorData) -> list:
    import aws_sdk_emr.types.string_map

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.string_map.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ErrorData:
    import aws_sdk_emr.types.string_map

    out: ErrorData = []
    for item in data:
        out.append(aws_sdk_emr.types.string_map.deserialize_aws_json_1_1(item))
    return out
