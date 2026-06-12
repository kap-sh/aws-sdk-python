"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CaptionSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.encryption
    import aws_sdk_elastic_transcoder.types.key
    import aws_sdk_elastic_transcoder.types.long_key
    import aws_sdk_elastic_transcoder.types.name
    import aws_sdk_elastic_transcoder.types.time_offset


class CaptionSource(TypedDict):
    key: NotRequired["aws_sdk_elastic_transcoder.types.long_key.LongKey"]
    """<p>The name of the sidecar caption file that you want Elastic Transcoder to include in the output file.</p>"""
    language: NotRequired["aws_sdk_elastic_transcoder.types.key.Key"]
    """<p>A string that specifies the language of the caption. If you specified multiple inputs with captions, the caption language must match in order to be included in the output. Specify this as one of:</p> <ul> <li> <p>2-character ISO 639-1 code</p> </li> <li> <p>3-character ISO 639-2 code</p> </li> </ul> <p>For more information on ISO language codes and language names, see the List of ISO 639-1 codes.</p>"""
    time_offset: NotRequired["aws_sdk_elastic_transcoder.types.time_offset.TimeOffset"]
    """<p>For clip generation or captions that do not start at the same time as the associated video file, the <code>TimeOffset</code> tells Elastic Transcoder how much of the video to encode before including captions.</p> <p>Specify the TimeOffset in the form [+-]SS.sss or [+-]HH:mm:SS.ss.</p>"""
    label: NotRequired["aws_sdk_elastic_transcoder.types.name.Name"]
    """<p>The label of the caption shown in the player when choosing a language. We recommend that you put the caption language name here, in the language of the captions.</p>"""
    encryption: NotRequired["aws_sdk_elastic_transcoder.types.encryption.Encryption"]
    """<p>The encryption settings, if any, that Elastic Transcoder needs to decyrpt your caption sources, or that you want Elastic Transcoder to apply to your caption sources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaptionSource) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "language" in value:
        out["Language"] = value["language"]
    if "time_offset" in value:
        out["TimeOffset"] = value["time_offset"]
    if "label" in value:
        out["Label"] = value["label"]
    if "encryption" in value:
        import aws_sdk_elastic_transcoder.types.encryption

        out["Encryption"] = aws_sdk_elastic_transcoder.types.encryption.serialize_json(
            value["encryption"]
        )
    return out


def deserialize_json(data: dict) -> CaptionSource:
    out: CaptionSource = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Language" in data:
        out["language"] = data["Language"]
    if "TimeOffset" in data:
        out["time_offset"] = data["TimeOffset"]
    if "Label" in data:
        out["label"] = data["Label"]
    if "Encryption" in data:
        import aws_sdk_elastic_transcoder.types.encryption

        out["encryption"] = (
            aws_sdk_elastic_transcoder.types.encryption.deserialize_json(
                data["Encryption"]
            )
        )
    return out
