"""Generated from Smithy shape ``com.amazonaws.datazone#AuthorizedPrincipalIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.authorized_principal_identifier

AuthorizedPrincipalIdentifiers: TypeAlias = list[
    "aws_sdk_datazone.types.authorized_principal_identifier.AuthorizedPrincipalIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizedPrincipalIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> AuthorizedPrincipalIdentifiers:
    return list(data)
