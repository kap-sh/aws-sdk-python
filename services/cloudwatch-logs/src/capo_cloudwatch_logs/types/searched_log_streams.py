"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SearchedLogStreams``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.searched_log_stream

SearchedLogStreams: TypeAlias = list[
    "capo_cloudwatch_logs.types.searched_log_stream.SearchedLogStream"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchedLogStreams) -> list:
    import capo_cloudwatch_logs.types.searched_log_stream

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.searched_log_stream.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SearchedLogStreams:
    import capo_cloudwatch_logs.types.searched_log_stream

    out: SearchedLogStreams = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.searched_log_stream.deserialize_aws_json_1_1(
                item
            )
        )
    return out
