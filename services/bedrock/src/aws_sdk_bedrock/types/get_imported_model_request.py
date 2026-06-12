"""Generated from Smithy shape ``com.amazonaws.bedrock#GetImportedModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.imported_model_identifier


class GetImportedModelRequest(TypedDict):
    model_identifier: (
        "aws_sdk_bedrock.types.imported_model_identifier.ImportedModelIdentifier"
    )
    """<p>Name or Amazon Resource Name (ARN) of the imported model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImportedModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImportedModelRequest:
    out: GetImportedModelRequest = {}  # type: ignore[typeddict-item]
    return out
