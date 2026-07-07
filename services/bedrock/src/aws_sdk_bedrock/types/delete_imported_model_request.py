"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteImportedModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.imported_model_identifier


class DeleteImportedModelRequest(TypedDict, closed=True):
    model_identifier: (
        "aws_sdk_bedrock.types.imported_model_identifier.ImportedModelIdentifier"
    )
    """<p>Name of the imported model to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImportedModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteImportedModelRequest:
    out: DeleteImportedModelRequest = {}  # type: ignore[typeddict-item]
    return out
