"""Generated from Smithy shape ``com.amazonaws.workspacesweb#InlineRedactionPatterns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.inline_redaction_pattern

InlineRedactionPatterns: TypeAlias = list[
    "aws_sdk_workspaces_web.types.inline_redaction_pattern.InlineRedactionPattern"
]


# --- restJson1 ser/de ---
def serialize_json(value: InlineRedactionPatterns) -> list:
    import aws_sdk_workspaces_web.types.inline_redaction_pattern

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces_web.types.inline_redaction_pattern.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InlineRedactionPatterns:
    import aws_sdk_workspaces_web.types.inline_redaction_pattern

    out: InlineRedactionPatterns = []
    for item in data:
        out.append(
            aws_sdk_workspaces_web.types.inline_redaction_pattern.deserialize_json(item)
        )
    return out
