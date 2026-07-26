"""Generated from Smithy shape ``com.amazonaws.appstream#CreateImageBuilderStreamingURLResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.string
    import capo_appstream.types.timestamp


class CreateImageBuilderStreamingURLResult(TypedDict, closed=True):
    streaming_url: NotRequired["capo_appstream.types.string.String"]
    """<p>The URL to start the WorkSpaces Applications streaming session.</p>"""
    expires: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The elapsed time, in seconds after the Unix epoch, when this URL expires.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImageBuilderStreamingURLResult) -> dict:
    out: dict = {}
    if "streaming_url" in value:
        out["StreamingURL"] = value["streaming_url"]
    if "expires" in value:
        import capo_appstream.types.timestamp

        out["Expires"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["expires"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateImageBuilderStreamingURLResult:
    out: CreateImageBuilderStreamingURLResult = {}  # type: ignore[typeddict-item]
    if "StreamingURL" in data:
        out["streaming_url"] = data["StreamingURL"]
    if "Expires" in data:
        import capo_appstream.types.timestamp

        out["expires"] = capo_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["Expires"]
        )
    return out
