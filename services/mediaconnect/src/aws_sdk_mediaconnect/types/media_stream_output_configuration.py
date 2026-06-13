"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaStreamOutputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_destination_configuration
    import aws_sdk_mediaconnect.types.encoding_name
    import aws_sdk_mediaconnect.types.encoding_parameters


class MediaStreamOutputConfiguration(TypedDict):
    destination_configurations: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_destination_configuration.__listOfDestinationConfiguration"
    ]
    """<p> The transport parameters that are associated with each outbound media stream.</p>"""
    encoding_name: NotRequired["aws_sdk_mediaconnect.types.encoding_name.EncodingName"]
    """<p> The format that was used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.</p>"""
    encoding_parameters: NotRequired[
        "aws_sdk_mediaconnect.types.encoding_parameters.EncodingParameters"
    ]
    """<p>A collection of parameters that determine how MediaConnect will convert the content. These fields only apply to outputs on flows that have a CDI source. </p>"""
    media_stream_name: NotRequired["str"]
    """<p> The name of the media stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamOutputConfiguration) -> dict:
    out: dict = {}
    if "destination_configurations" in value:
        import aws_sdk_mediaconnect.types.__list_of_destination_configuration

        out["destinationConfigurations"] = (
            aws_sdk_mediaconnect.types.__list_of_destination_configuration.serialize_json(
                value["destination_configurations"]
            )
        )
    if "encoding_name" in value:
        import aws_sdk_mediaconnect.types.encoding_name

        out["encodingName"] = aws_sdk_mediaconnect.types.encoding_name.serialize_json(
            value["encoding_name"]
        )
    if "encoding_parameters" in value:
        import aws_sdk_mediaconnect.types.encoding_parameters

        out["encodingParameters"] = (
            aws_sdk_mediaconnect.types.encoding_parameters.serialize_json(
                value["encoding_parameters"]
            )
        )
    if "media_stream_name" in value:
        out["mediaStreamName"] = value["media_stream_name"]
    return out


def deserialize_json(data: dict) -> MediaStreamOutputConfiguration:
    out: MediaStreamOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "destinationConfigurations" in data:
        import aws_sdk_mediaconnect.types.__list_of_destination_configuration

        out["destination_configurations"] = (
            aws_sdk_mediaconnect.types.__list_of_destination_configuration.deserialize_json(
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
        import aws_sdk_mediaconnect.types.encoding_parameters

        out["encoding_parameters"] = (
            aws_sdk_mediaconnect.types.encoding_parameters.deserialize_json(
                data["encodingParameters"]
            )
        )
    if "mediaStreamName" in data:
        out["media_stream_name"] = data["mediaStreamName"]
    return out
