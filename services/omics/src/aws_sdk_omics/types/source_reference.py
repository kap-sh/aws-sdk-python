"""Generated from Smithy shape ``com.amazonaws.omics#SourceReference``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.source_reference_type
    import aws_sdk_omics.types.source_reference_value


class SourceReference(TypedDict):
    type: "aws_sdk_omics.types.source_reference_type.SourceReferenceType"
    """<p>The type of source reference, such as branch, tag, or commit.</p>"""
    value: "aws_sdk_omics.types.source_reference_value.SourceReferenceValue"
    """<p>The value of the source reference, such as the branch name, tag name, or commit ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceReference) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SourceReference:
    out: SourceReference = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SourceReference.type required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("SourceReference.value required")
    return out
