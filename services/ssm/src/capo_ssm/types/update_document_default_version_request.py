"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateDocumentDefaultVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.document_name
    import capo_ssm.types.document_version_number


class UpdateDocumentDefaultVersionRequest(TypedDict, closed=True):
    name: "capo_ssm.types.document_name.DocumentName"
    """<p>The name of a custom document that you want to set as the default version.</p>"""
    document_version: "capo_ssm.types.document_version_number.DocumentVersionNumber"
    """<p>The version of a custom document that you want to set as the default version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDocumentDefaultVersionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["DocumentVersion"] = value["document_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDocumentDefaultVersionRequest:
    out: UpdateDocumentDefaultVersionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDocumentDefaultVersionRequest.name required")
    if "DocumentVersion" in data:
        out["document_version"] = data["DocumentVersion"]
    else:
        raise DeserializationError(
            "UpdateDocumentDefaultVersionRequest.document_version required"
        )
    return out
