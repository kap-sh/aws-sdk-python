"""Generated from Smithy shape ``com.amazonaws.connecthealth#TemplateSectionInstruction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.sensitive_alphanumeric_string
    import aws_sdk_connecthealth.types.sensitive_markdown_string


class TemplateSectionInstruction(TypedDict, closed=True):
    section_header: "aws_sdk_connecthealth.types.sensitive_alphanumeric_string.SensitiveAlphanumericString"
    """<p>The header for this section of the template</p>"""
    section_instruction: (
        "aws_sdk_connecthealth.types.sensitive_markdown_string.SensitiveMarkdownString"
    )
    """<p>The instruction for generating this section</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSectionInstruction) -> dict:
    out: dict = {}
    out["sectionHeader"] = value["section_header"]
    out["sectionInstruction"] = value["section_instruction"]
    return out


def deserialize_json(data: dict) -> TemplateSectionInstruction:
    out: TemplateSectionInstruction = {}  # type: ignore[typeddict-item]
    if "sectionHeader" in data:
        out["section_header"] = data["sectionHeader"]
    else:
        raise DeserializationError("TemplateSectionInstruction.section_header required")
    if "sectionInstruction" in data:
        out["section_instruction"] = data["sectionInstruction"]
    else:
        raise DeserializationError(
            "TemplateSectionInstruction.section_instruction required"
        )
    return out
