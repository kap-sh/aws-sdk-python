"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteImportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id


class DeleteImportRequest(TypedDict, closed=True):
    import_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the import to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteImportRequest:
    out: DeleteImportRequest = {}  # type: ignore[typeddict-item]
    return out
