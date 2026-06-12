"""Generated from Smithy shape ``com.amazonaws.rdsdata#UpdateResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.update_result

UpdateResults: TypeAlias = list["aws_sdk_rds_data.types.update_result.UpdateResult"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResults) -> list:
    import aws_sdk_rds_data.types.update_result

    out: list = []
    for item in value:
        out.append(aws_sdk_rds_data.types.update_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateResults:
    import aws_sdk_rds_data.types.update_result

    out: UpdateResults = []
    for item in data:
        out.append(aws_sdk_rds_data.types.update_result.deserialize_json(item))
    return out
