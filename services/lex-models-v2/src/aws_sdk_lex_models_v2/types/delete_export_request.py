"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteExportRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id


class DeleteExportRequest(TypedDict):
    export_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the export to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteExportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteExportRequest:
    out: DeleteExportRequest = {}  # type: ignore[typeddict-item]
    return out
