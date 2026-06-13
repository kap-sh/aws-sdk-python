"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaStreamSourceConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_input_configuration_request
    import aws_sdk_mediaconnect.types.encoding_name


class MediaStreamSourceConfigurationRequest(TypedDict):
    encoding_name: NotRequired["aws_sdk_mediaconnect.types.encoding_name.EncodingName"]
    """<p>The format that was used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv. </p>"""
    input_configurations: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_input_configuration_request.__listOfInputConfigurationRequest"
    ]
    """<p>The media streams that you want to associate with the source. </p>"""
    media_stream_name: NotRequired["str"]
    """<p>The name of the media stream. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamSourceConfigurationRequest) -> dict:
    out: dict = {}
    if "encoding_name" in value:
        import aws_sdk_mediaconnect.types.encoding_name

        out["encodingName"] = aws_sdk_mediaconnect.types.encoding_name.serialize_json(
            value["encoding_name"]
        )
    if "input_configurations" in value:
        import aws_sdk_mediaconnect.types.__list_of_input_configuration_request

        out["inputConfigurations"] = (
            aws_sdk_mediaconnect.types.__list_of_input_configuration_request.serialize_json(
                value["input_configurations"]
            )
        )
    if "media_stream_name" in value:
        out["mediaStreamName"] = value["media_stream_name"]
    return out


def deserialize_json(data: dict) -> MediaStreamSourceConfigurationRequest:
    out: MediaStreamSourceConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "encodingName" in data:
        import aws_sdk_mediaconnect.types.encoding_name

        out["encoding_name"] = (
            aws_sdk_mediaconnect.types.encoding_name.deserialize_json(
                data["encodingName"]
            )
        )
    if "inputConfigurations" in data:
        import aws_sdk_mediaconnect.types.__list_of_input_configuration_request

        out["input_configurations"] = (
            aws_sdk_mediaconnect.types.__list_of_input_configuration_request.deserialize_json(
                data["inputConfigurations"]
            )
        )
    if "mediaStreamName" in data:
        out["media_stream_name"] = data["mediaStreamName"]
    return out
