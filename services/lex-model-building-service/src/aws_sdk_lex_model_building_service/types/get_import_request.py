"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetImportRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.string


class GetImportRequest(TypedDict):
    import_id: "aws_sdk_lex_model_building_service.types.string.String"
    """<p>The identifier of the import job information to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImportRequest:
    out: GetImportRequest = {}  # type: ignore[typeddict-item]
    return out
