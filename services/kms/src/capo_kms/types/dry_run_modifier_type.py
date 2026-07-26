"""Generated from Smithy shape ``com.amazonaws.kms#DryRunModifierType``."""

from typing import Literal, TypeAlias, cast

DryRunModifierType: TypeAlias = Literal["IGNORE_CIPHERTEXT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DryRunModifierType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DryRunModifierType:
    return cast(DryRunModifierType, data)
