"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.import_export_file_password


class UpdateExportRequest(TypedDict, closed=True):
    export_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier Amazon Lex assigned to the export.</p>"""
    file_password: NotRequired[
        "aws_sdk_lex_models_v2.types.import_export_file_password.ImportExportFilePassword"
    ]
    """<p>The new password to use to encrypt the export zip archive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExportRequest) -> dict:
    out: dict = {}
    if "file_password" in value:
        out["filePassword"] = value["file_password"]
    return out


def deserialize_json(data: dict) -> UpdateExportRequest:
    out: UpdateExportRequest = {}  # type: ignore[typeddict-item]
    if "filePassword" in data:
        out["file_password"] = data["filePassword"]
    return out
