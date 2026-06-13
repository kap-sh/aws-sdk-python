"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrieveResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.reference_type
    import aws_sdk_qconnect.types.sensitive_string
    import aws_sdk_qconnect.types.uuid


class RetrieveResult(TypedDict):
    association_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the assistant association for the retrieved result.</p>"""
    source_id: "aws_sdk_qconnect.types.sensitive_string.SensitiveString"
    """<p>The URL, URI, or ID of the retrieved content when available, or a UUID when unavailable.</p>"""
    reference_type: "aws_sdk_qconnect.types.reference_type.ReferenceType"
    """<p>A type to define the KB origin of a retrieved content.</p>"""
    content_text: "aws_sdk_qconnect.types.sensitive_string.SensitiveString"
    """<p>The text content of the retrieved result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveResult) -> dict:
    out: dict = {}
    out["associationId"] = value["association_id"]
    out["sourceId"] = value["source_id"]
    out["referenceType"] = value["reference_type"]
    out["contentText"] = value["content_text"]
    return out


def deserialize_json(data: dict) -> RetrieveResult:
    out: RetrieveResult = {}  # type: ignore[typeddict-item]
    if "associationId" in data:
        out["association_id"] = data["associationId"]
    else:
        raise DeserializationError("RetrieveResult.association_id required")
    if "sourceId" in data:
        out["source_id"] = data["sourceId"]
    else:
        raise DeserializationError("RetrieveResult.source_id required")
    if "referenceType" in data:
        out["reference_type"] = data["referenceType"]
    else:
        raise DeserializationError("RetrieveResult.reference_type required")
    if "contentText" in data:
        out["content_text"] = data["contentText"]
    else:
        raise DeserializationError("RetrieveResult.content_text required")
    return out
