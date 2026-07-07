"""Generated from Smithy shape ``com.amazonaws.rekognition#ListStreamProcessorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.pagination_token
    import aws_sdk_rekognition.types.stream_processor_list


class ListStreamProcessorsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_rekognition.types.pagination_token.PaginationToken"
    ]
    """<p>If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of stream processors. </p>"""
    stream_processors: NotRequired[
        "aws_sdk_rekognition.types.stream_processor_list.StreamProcessorList"
    ]
    """<p>List of stream processors that you have created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStreamProcessorsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "stream_processors" in value:
        import aws_sdk_rekognition.types.stream_processor_list

        out["StreamProcessors"] = (
            aws_sdk_rekognition.types.stream_processor_list.serialize_aws_json_1_1(
                value["stream_processors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStreamProcessorsResponse:
    out: ListStreamProcessorsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "StreamProcessors" in data:
        import aws_sdk_rekognition.types.stream_processor_list

        out["stream_processors"] = (
            aws_sdk_rekognition.types.stream_processor_list.deserialize_aws_json_1_1(
                data["StreamProcessors"]
            )
        )
    return out
