"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#ListStreamsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.stream_arn_token
    import aws_sdk_keyspacesstreams.types.stream_list


class ListStreamsOutput(TypedDict):
    streams: NotRequired["aws_sdk_keyspacesstreams.types.stream_list.StreamList"]
    """<p> An array of stream objects, each containing summary information about a stream including its ARN, status, and associated table information. This list includes all streams that match the request criteria. </p>"""
    next_token: NotRequired[
        "aws_sdk_keyspacesstreams.types.stream_arn_token.StreamArnToken"
    ]
    """<p> A pagination token that can be used in a subsequent <code>ListStreams</code> request. This token is returned if the response contains more streams than can be returned in a single response based on the <code>maxResults</code> parameter. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListStreamsOutput) -> dict:
    out: dict = {}
    if "streams" in value:
        import aws_sdk_keyspacesstreams.types.stream_list

        out["streams"] = (
            aws_sdk_keyspacesstreams.types.stream_list.serialize_aws_json_1_0(
                value["streams"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListStreamsOutput:
    out: ListStreamsOutput = {}  # type: ignore[typeddict-item]
    if "streams" in data:
        import aws_sdk_keyspacesstreams.types.stream_list

        out["streams"] = (
            aws_sdk_keyspacesstreams.types.stream_list.deserialize_aws_json_1_0(
                data["streams"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
