"""Generated from Smithy shape ``com.amazonaws.lakeformation#RemoveLFTagsFromResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.lf_tag_errors


class RemoveLFTagsFromResourceResponse(TypedDict, closed=True):
    failures: NotRequired["capo_lakeformation.types.lf_tag_errors.LFTagErrors"]
    """<p>A list of failures to untag a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveLFTagsFromResourceResponse) -> dict:
    out: dict = {}
    if "failures" in value:
        import capo_lakeformation.types.lf_tag_errors

        out["Failures"] = capo_lakeformation.types.lf_tag_errors.serialize_json(
            value["failures"]
        )
    return out


def deserialize_json(data: dict) -> RemoveLFTagsFromResourceResponse:
    out: RemoveLFTagsFromResourceResponse = {}  # type: ignore[typeddict-item]
    if "Failures" in data:
        import capo_lakeformation.types.lf_tag_errors

        out["failures"] = capo_lakeformation.types.lf_tag_errors.deserialize_json(
            data["Failures"]
        )
    return out
