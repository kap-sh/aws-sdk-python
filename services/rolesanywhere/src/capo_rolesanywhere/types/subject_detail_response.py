"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#SubjectDetailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.subject_detail


class SubjectDetailResponse(TypedDict, closed=True):
    subject: NotRequired["capo_rolesanywhere.types.subject_detail.SubjectDetail"]
    """<p>The state of the subject after a read or write operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubjectDetailResponse) -> dict:
    out: dict = {}
    if "subject" in value:
        import capo_rolesanywhere.types.subject_detail

        out["subject"] = capo_rolesanywhere.types.subject_detail.serialize_json(
            value["subject"]
        )
    return out


def deserialize_json(data: dict) -> SubjectDetailResponse:
    out: SubjectDetailResponse = {}  # type: ignore[typeddict-item]
    if "subject" in data:
        import capo_rolesanywhere.types.subject_detail

        out["subject"] = capo_rolesanywhere.types.subject_detail.deserialize_json(
            data["subject"]
        )
    return out
