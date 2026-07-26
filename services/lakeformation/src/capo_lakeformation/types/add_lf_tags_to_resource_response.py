"""Generated from Smithy shape ``com.amazonaws.lakeformation#AddLFTagsToResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.lf_tag_errors


class AddLFTagsToResourceResponse(TypedDict, closed=True):
    failures: NotRequired["capo_lakeformation.types.lf_tag_errors.LFTagErrors"]
    """<p>A list of failures to tag the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddLFTagsToResourceResponse) -> dict:
    out: dict = {}
    if "failures" in value:
        import capo_lakeformation.types.lf_tag_errors

        out["Failures"] = capo_lakeformation.types.lf_tag_errors.serialize_json(
            value["failures"]
        )
    return out


def deserialize_json(data: dict) -> AddLFTagsToResourceResponse:
    out: AddLFTagsToResourceResponse = {}  # type: ignore[typeddict-item]
    if "Failures" in data:
        import capo_lakeformation.types.lf_tag_errors

        out["failures"] = capo_lakeformation.types.lf_tag_errors.deserialize_json(
            data["Failures"]
        )
    return out
