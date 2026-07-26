"""Generated from Smithy shape ``com.amazonaws.emr#ErrorData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.string_map

ErrorData: TypeAlias = list["capo_emr.types.string_map.StringMap"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorData) -> list:
    import capo_emr.types.string_map

    out: list = []
    for item in value:
        out.append(capo_emr.types.string_map.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ErrorData:
    import capo_emr.types.string_map

    out: ErrorData = []
    for item in data:
        out.append(capo_emr.types.string_map.deserialize_aws_json_1_1(item))
    return out
