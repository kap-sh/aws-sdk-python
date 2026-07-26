"""Generated from Smithy shape ``com.amazonaws.identitystore#ExtensionNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.extension_name

ExtensionNames: TypeAlias = list[
    "capo_identitystore.types.extension_name.ExtensionName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtensionNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExtensionNames:
    return list(data)
