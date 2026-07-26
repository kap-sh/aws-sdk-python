"""Generated from Smithy shape ``com.amazonaws.rdsdata#UpdateResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rds_data.types.update_result

UpdateResults: TypeAlias = list["capo_rds_data.types.update_result.UpdateResult"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResults) -> list:
    import capo_rds_data.types.update_result

    out: list = []
    for item in value:
        out.append(capo_rds_data.types.update_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateResults:
    import capo_rds_data.types.update_result

    out: UpdateResults = []
    for item in data:
        out.append(capo_rds_data.types.update_result.deserialize_json(item))
    return out
