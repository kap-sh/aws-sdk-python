"""Generated from Smithy shape ``com.amazonaws.signerdata#RevokedEntities``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_signer_data.types.revoked_entity

RevokedEntities: TypeAlias = list["aws_sdk_signer_data.types.revoked_entity.RevokedEntity"]


# --- restJson1 ser/de ---
def serialize_json(value: RevokedEntities) -> list:
    return list(value)


def deserialize_json(data: list) -> RevokedEntities:
    return list(data)