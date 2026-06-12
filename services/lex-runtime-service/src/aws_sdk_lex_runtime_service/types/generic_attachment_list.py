"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#genericAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.generic_attachment

genericAttachmentList: TypeAlias = list[
    "aws_sdk_lex_runtime_service.types.generic_attachment.GenericAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: genericAttachmentList) -> list:
    import aws_sdk_lex_runtime_service.types.generic_attachment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_runtime_service.types.generic_attachment.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> genericAttachmentList:
    import aws_sdk_lex_runtime_service.types.generic_attachment

    out: genericAttachmentList = []
    for item in data:
        out.append(
            aws_sdk_lex_runtime_service.types.generic_attachment.deserialize_json(item)
        )
    return out
