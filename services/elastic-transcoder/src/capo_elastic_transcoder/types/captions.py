"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Captions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.caption_formats
    import capo_elastic_transcoder.types.caption_merge_policy
    import capo_elastic_transcoder.types.caption_sources


class Captions(TypedDict, closed=True):
    merge_policy: NotRequired[
        "capo_elastic_transcoder.types.caption_merge_policy.CaptionMergePolicy"
    ]
    """<p>A policy that determines how Elastic Transcoder handles the existence of multiple captions.</p> <ul> <li> <p> <b>MergeOverride:</b> Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the sidecar captions and ignores the embedded captions for that language.</p> </li> <li> <p> <b>MergeRetain:</b> Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the embedded captions and ignores the sidecar captions for that language. If <code>CaptionSources</code> is empty, Elastic Transcoder omits all sidecar captions from the output files.</p> </li> <li> <p> <b>Override:</b> Elastic Transcoder transcodes only the sidecar captions that you specify in <code>CaptionSources</code>.</p> </li> </ul> <p> <code>MergePolicy</code> cannot be null.</p>"""
    caption_sources: NotRequired[
        "capo_elastic_transcoder.types.caption_sources.CaptionSources"
    ]
    """<p>Source files for the input sidecar captions used during the transcoding process. To omit all sidecar captions, leave <code>CaptionSources</code> blank.</p>"""
    caption_formats: NotRequired[
        "capo_elastic_transcoder.types.caption_formats.CaptionFormats"
    ]
    """<p>The array of file formats for the output captions. If you leave this value blank, Elastic Transcoder returns an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Captions) -> dict:
    out: dict = {}
    if "merge_policy" in value:
        out["MergePolicy"] = value["merge_policy"]
    if "caption_sources" in value:
        import capo_elastic_transcoder.types.caption_sources

        out["CaptionSources"] = (
            capo_elastic_transcoder.types.caption_sources.serialize_json(
                value["caption_sources"]
            )
        )
    if "caption_formats" in value:
        import capo_elastic_transcoder.types.caption_formats

        out["CaptionFormats"] = (
            capo_elastic_transcoder.types.caption_formats.serialize_json(
                value["caption_formats"]
            )
        )
    return out


def deserialize_json(data: dict) -> Captions:
    out: Captions = {}  # type: ignore[typeddict-item]
    if "MergePolicy" in data:
        out["merge_policy"] = data["MergePolicy"]
    if "CaptionSources" in data:
        import capo_elastic_transcoder.types.caption_sources

        out["caption_sources"] = (
            capo_elastic_transcoder.types.caption_sources.deserialize_json(
                data["CaptionSources"]
            )
        )
    if "CaptionFormats" in data:
        import capo_elastic_transcoder.types.caption_formats

        out["caption_formats"] = (
            capo_elastic_transcoder.types.caption_formats.deserialize_json(
                data["CaptionFormats"]
            )
        )
    return out
