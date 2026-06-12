"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#UnprocessedEndTimeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.list_of_timestamps

UnprocessedEndTimeMap: TypeAlias = dict[
    "str", "aws_sdk_codeguruprofiler.types.list_of_timestamps.ListOfTimestamps"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UnprocessedEndTimeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_codeguruprofiler.types.list_of_timestamps

        out[key] = aws_sdk_codeguruprofiler.types.list_of_timestamps.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> UnprocessedEndTimeMap:
    out: UnprocessedEndTimeMap = {}
    for key, value in data.items():
        import aws_sdk_codeguruprofiler.types.list_of_timestamps

        out[key] = aws_sdk_codeguruprofiler.types.list_of_timestamps.deserialize_json(
            value
        )
    return out
