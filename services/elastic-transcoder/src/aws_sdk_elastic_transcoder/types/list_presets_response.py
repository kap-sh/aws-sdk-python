"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#ListPresetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.id
    import aws_sdk_elastic_transcoder.types.presets


class ListPresetsResponse(TypedDict):
    presets: NotRequired["aws_sdk_elastic_transcoder.types.presets.Presets"]
    """<p>An array of <code>Preset</code> objects.</p>"""
    next_page_token: NotRequired["aws_sdk_elastic_transcoder.types.id.Id"]
    """<p>A value that you use to access the second and subsequent pages of results, if any. When the presets fit on one page or when you've reached the last page of results, the value of <code>NextPageToken</code> is <code>null</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPresetsResponse) -> dict:
    out: dict = {}
    if "presets" in value:
        import aws_sdk_elastic_transcoder.types.presets

        out["Presets"] = aws_sdk_elastic_transcoder.types.presets.serialize_json(
            value["presets"]
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_json(data: dict) -> ListPresetsResponse:
    out: ListPresetsResponse = {}  # type: ignore[typeddict-item]
    if "Presets" in data:
        import aws_sdk_elastic_transcoder.types.presets

        out["presets"] = aws_sdk_elastic_transcoder.types.presets.deserialize_json(
            data["Presets"]
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
