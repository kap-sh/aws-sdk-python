"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#ResultErrorEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail_data.types.result_error_entry

ResultErrorEntries: TypeAlias = list[
    "capo_cloudtrail_data.types.result_error_entry.ResultErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResultErrorEntries) -> list:
    import capo_cloudtrail_data.types.result_error_entry

    out: list = []
    for item in value:
        out.append(capo_cloudtrail_data.types.result_error_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResultErrorEntries:
    import capo_cloudtrail_data.types.result_error_entry

    out: ResultErrorEntries = []
    for item in data:
        out.append(capo_cloudtrail_data.types.result_error_entry.deserialize_json(item))
    return out
