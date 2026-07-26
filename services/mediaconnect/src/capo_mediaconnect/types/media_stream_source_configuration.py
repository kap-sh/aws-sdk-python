"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaStreamSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_input_configuration
    import capo_mediaconnect.types.encoding_name


class MediaStreamSourceConfiguration(TypedDict, closed=True):
    encoding_name: NotRequired["capo_mediaconnect.types.encoding_name.EncodingName"]
    """<p> The format that was used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv. </p>"""
    input_configurations: NotRequired[
        "capo_mediaconnect.types.__list_of_input_configuration.__listOfInputConfiguration"
    ]
    """<p>The media streams that you want to associate with the source. </p>"""
    media_stream_name: NotRequired["str"]
    """<p>A name that helps you distinguish one media stream from another. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamSourceConfiguration) -> dict:
    out: dict = {}
    if "encoding_name" in value:
        import capo_mediaconnect.types.encoding_name

        out["encodingName"] = capo_mediaconnect.types.encoding_name.serialize_json(
            value["encoding_name"]
        )
    if "input_configurations" in value:
        import capo_mediaconnect.types.__list_of_input_configuration

        out["inputConfigurations"] = (
            capo_mediaconnect.types.__list_of_input_configuration.serialize_json(
                value["input_configurations"]
            )
        )
    if "media_stream_name" in value:
        out["mediaStreamName"] = value["media_stream_name"]
    return out


def deserialize_json(data: dict) -> MediaStreamSourceConfiguration:
    out: MediaStreamSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "encodingName" in data:
        import capo_mediaconnect.types.encoding_name

        out["encoding_name"] = capo_mediaconnect.types.encoding_name.deserialize_json(
            data["encodingName"]
        )
    if "inputConfigurations" in data:
        import capo_mediaconnect.types.__list_of_input_configuration

        out["input_configurations"] = (
            capo_mediaconnect.types.__list_of_input_configuration.deserialize_json(
                data["inputConfigurations"]
            )
        )
    if "mediaStreamName" in data:
        out["media_stream_name"] = data["mediaStreamName"]
    return out
