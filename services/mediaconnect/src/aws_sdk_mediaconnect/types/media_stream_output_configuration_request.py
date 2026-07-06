"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaStreamOutputConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_destination_configuration_request
    import aws_sdk_mediaconnect.types.encoding_name
    import aws_sdk_mediaconnect.types.encoding_parameters_request


class MediaStreamOutputConfigurationRequest(TypedDict, closed=True):
    destination_configurations: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_destination_configuration_request.__listOfDestinationConfigurationRequest"
    ]
    """<p> The media streams that you want to associate with the output. </p>"""
    encoding_name: NotRequired["aws_sdk_mediaconnect.types.encoding_name.EncodingName"]
    """<p> The format that will be used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.</p>"""
    encoding_parameters: NotRequired[
        "aws_sdk_mediaconnect.types.encoding_parameters_request.EncodingParametersRequest"
    ]
    """<p> A collection of parameters that determine how MediaConnect will convert the content. These fields only apply to outputs on flows that have a CDI source. </p>"""
    media_stream_name: NotRequired["str"]
    """<p> The name of the media stream that is associated with the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamOutputConfigurationRequest) -> dict:
    out: dict = {}
    if "destination_configurations" in value:
        import aws_sdk_mediaconnect.types.__list_of_destination_configuration_request

        out["destinationConfigurations"] = (
            aws_sdk_mediaconnect.types.__list_of_destination_configuration_request.serialize_json(
                value["destination_configurations"]
            )
        )
    if "encoding_name" in value:
        import aws_sdk_mediaconnect.types.encoding_name

        out["encodingName"] = aws_sdk_mediaconnect.types.encoding_name.serialize_json(
            value["encoding_name"]
        )
    if "encoding_parameters" in value:
        import aws_sdk_mediaconnect.types.encoding_parameters_request

        out["encodingParameters"] = (
            aws_sdk_mediaconnect.types.encoding_parameters_request.serialize_json(
                value["encoding_parameters"]
            )
        )
    if "media_stream_name" in value:
        out["mediaStreamName"] = value["media_stream_name"]
    return out


def deserialize_json(data: dict) -> MediaStreamOutputConfigurationRequest:
    out: MediaStreamOutputConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "destinationConfigurations" in data:
        import aws_sdk_mediaconnect.types.__list_of_destination_configuration_request

        out["destination_configurations"] = (
            aws_sdk_mediaconnect.types.__list_of_destination_configuration_request.deserialize_json(
                data["destinationConfigurations"]
            )
        )
    if "encodingName" in data:
        import aws_sdk_mediaconnect.types.encoding_name

        out["encoding_name"] = (
            aws_sdk_mediaconnect.types.encoding_name.deserialize_json(
                data["encodingName"]
            )
        )
    if "encodingParameters" in data:
        import aws_sdk_mediaconnect.types.encoding_parameters_request

        out["encoding_parameters"] = (
            aws_sdk_mediaconnect.types.encoding_parameters_request.deserialize_json(
                data["encodingParameters"]
            )
        )
    if "mediaStreamName" in data:
        out["media_stream_name"] = data["mediaStreamName"]
    return out
