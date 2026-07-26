"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ScalarSubjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.uuid


class ScalarSubjectRequest(TypedDict, closed=True):
    subject_id: "capo_rolesanywhere.types.uuid.Uuid"
    """<p>The unique identifier of the subject. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScalarSubjectRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ScalarSubjectRequest:
    out: ScalarSubjectRequest = {}  # type: ignore[typeddict-item]
    return out
