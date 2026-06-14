"""Generated from Smithy shape ``com.amazonaws.workspacesweb#EncryptionContextMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.string_type

EncryptionContextMap: TypeAlias = dict[
    "aws_sdk_workspaces_web.types.string_type.StringType",
    "aws_sdk_workspaces_web.types.string_type.StringType",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EncryptionContextMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EncryptionContextMap:
    out: EncryptionContextMap = {}
    for key, value in data.items():
        out[key] = value
    return out
