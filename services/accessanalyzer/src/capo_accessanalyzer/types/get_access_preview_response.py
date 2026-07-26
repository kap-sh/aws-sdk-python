"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetAccessPreviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.access_preview


class GetAccessPreviewResponse(TypedDict, closed=True):
    access_preview: "capo_accessanalyzer.types.access_preview.AccessPreview"
    """<p>An object that contains information about the access preview.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessPreviewResponse) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.access_preview

    out["accessPreview"] = capo_accessanalyzer.types.access_preview.serialize_json(
        value["access_preview"]
    )
    return out


def deserialize_json(data: dict) -> GetAccessPreviewResponse:
    out: GetAccessPreviewResponse = {}  # type: ignore[typeddict-item]
    if "accessPreview" in data:
        import capo_accessanalyzer.types.access_preview

        out["access_preview"] = (
            capo_accessanalyzer.types.access_preview.deserialize_json(
                data["accessPreview"]
            )
        )
    else:
        raise DeserializationError("GetAccessPreviewResponse.access_preview required")
    return out
