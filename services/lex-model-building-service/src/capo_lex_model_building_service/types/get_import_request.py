"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetImportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.string


class GetImportRequest(TypedDict, closed=True):
    import_id: "capo_lex_model_building_service.types.string.String"
    """<p>The identifier of the import job information to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImportRequest:
    out: GetImportRequest = {}  # type: ignore[typeddict-item]
    return out
