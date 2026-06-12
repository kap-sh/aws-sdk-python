"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#GetDataEndpointInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.api_name
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.stream_name


class GetDataEndpointInput(TypedDict):
    stream_name: NotRequired["aws_sdk_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream that you want to get the endpoint for. You must specify either this parameter or a <code>StreamARN</code> in the request.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream that you want to get the endpoint for. You must specify either this parameter or a <code>StreamName</code> in the request. </p>"""
    api_name: "aws_sdk_kinesis_video.types.api_name.APIName"
    """<p>The name of the API action for which to get an endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataEndpointInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    import aws_sdk_kinesis_video.types.api_name

    out["APIName"] = aws_sdk_kinesis_video.types.api_name.serialize_json(
        value["api_name"]
    )
    return out


def deserialize_json(data: dict) -> GetDataEndpointInput:
    out: GetDataEndpointInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "APIName" in data:
        import aws_sdk_kinesis_video.types.api_name

        out["api_name"] = aws_sdk_kinesis_video.types.api_name.deserialize_json(
            data["APIName"]
        )
    else:
        raise DeserializationError("GetDataEndpointInput.api_name required")
    return out
