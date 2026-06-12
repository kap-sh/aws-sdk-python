"""Generated from Smithy shape ``com.amazonaws.amplify#AutoSubDomainCreationPatterns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplify.types.auto_sub_domain_creation_pattern

AutoSubDomainCreationPatterns: TypeAlias = list[
    "aws_sdk_amplify.types.auto_sub_domain_creation_pattern.AutoSubDomainCreationPattern"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoSubDomainCreationPatterns) -> list:
    return list(value)


def deserialize_json(data: list) -> AutoSubDomainCreationPatterns:
    return list(data)
