"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenFeatureFlags``."""

from typing import TypedDict

from typing_extensions import NotRequired


class CodegenFeatureFlags(TypedDict):
    is_relationship_supported: NotRequired["bool"]
    """<p>Specifes whether a code generation job supports data relationships.</p>"""
    is_non_model_supported: NotRequired["bool"]
    """<p>Specifies whether a code generation job supports non models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenFeatureFlags) -> dict:
    out: dict = {}
    if "is_relationship_supported" in value:
        out["isRelationshipSupported"] = value["is_relationship_supported"]
    if "is_non_model_supported" in value:
        out["isNonModelSupported"] = value["is_non_model_supported"]
    return out


def deserialize_json(data: dict) -> CodegenFeatureFlags:
    out: CodegenFeatureFlags = {}  # type: ignore[typeddict-item]
    if "isRelationshipSupported" in data:
        out["is_relationship_supported"] = data["isRelationshipSupported"]
    if "isNonModelSupported" in data:
        out["is_non_model_supported"] = data["isNonModelSupported"]
    return out
