"""Generated from Smithy shape ``com.amazonaws.repostspace#AllowedDomainsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.email_domain

AllowedDomainsList: TypeAlias = list[
    "aws_sdk_repostspace.types.email_domain.EmailDomain"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedDomainsList) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedDomainsList:
    return list(data)
