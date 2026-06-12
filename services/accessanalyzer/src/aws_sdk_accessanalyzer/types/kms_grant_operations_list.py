"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#KmsGrantOperationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.kms_grant_operation

KmsGrantOperationsList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.kms_grant_operation.KmsGrantOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: KmsGrantOperationsList) -> list:
    return list(value)


def deserialize_json(data: list) -> KmsGrantOperationsList:
    return list(data)
