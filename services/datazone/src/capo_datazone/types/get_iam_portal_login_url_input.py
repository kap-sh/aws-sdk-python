"""Generated from Smithy shape ``com.amazonaws.datazone#GetIamPortalLoginUrlInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id


class GetIamPortalLoginUrlInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>the ID of the Amazon DataZone domain the data portal of which you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIamPortalLoginUrlInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIamPortalLoginUrlInput:
    out: GetIamPortalLoginUrlInput = {}  # type: ignore[typeddict-item]
    return out
