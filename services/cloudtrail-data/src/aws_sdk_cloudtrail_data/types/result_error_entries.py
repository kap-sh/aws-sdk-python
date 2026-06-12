"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#ResultErrorEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail_data.types.result_error_entry

ResultErrorEntries: TypeAlias = list[
    "aws_sdk_cloudtrail_data.types.result_error_entry.ResultErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResultErrorEntries) -> list:
    import aws_sdk_cloudtrail_data.types.result_error_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudtrail_data.types.result_error_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResultErrorEntries:
    import aws_sdk_cloudtrail_data.types.result_error_entry

    out: ResultErrorEntries = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail_data.types.result_error_entry.deserialize_json(item)
        )
    return out
