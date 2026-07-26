"""Generated from Smithy shape ``com.amazonaws.lakeformation#LFTagError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.error_detail
    import capo_lakeformation.types.lf_tag_pair


class LFTagError(TypedDict, closed=True):
    lf_tag: NotRequired["capo_lakeformation.types.lf_tag_pair.LFTagPair"]
    """<p>The key-name of the LF-tag.</p>"""
    error: NotRequired["capo_lakeformation.types.error_detail.ErrorDetail"]
    """<p>An error that occurred with the attachment or detachment of the LF-tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LFTagError) -> dict:
    out: dict = {}
    if "lf_tag" in value:
        import capo_lakeformation.types.lf_tag_pair

        out["LFTag"] = capo_lakeformation.types.lf_tag_pair.serialize_json(
            value["lf_tag"]
        )
    if "error" in value:
        import capo_lakeformation.types.error_detail

        out["Error"] = capo_lakeformation.types.error_detail.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> LFTagError:
    out: LFTagError = {}  # type: ignore[typeddict-item]
    if "LFTag" in data:
        import capo_lakeformation.types.lf_tag_pair

        out["lf_tag"] = capo_lakeformation.types.lf_tag_pair.deserialize_json(
            data["LFTag"]
        )
    if "Error" in data:
        import capo_lakeformation.types.error_detail

        out["error"] = capo_lakeformation.types.error_detail.deserialize_json(
            data["Error"]
        )
    return out
