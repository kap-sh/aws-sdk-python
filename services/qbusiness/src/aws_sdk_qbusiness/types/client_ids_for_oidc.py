"""Generated from Smithy shape ``com.amazonaws.qbusiness#ClientIdsForOIDC``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.client_id_for_oidc

ClientIdsForOIDC: TypeAlias = list[
    "aws_sdk_qbusiness.types.client_id_for_oidc.ClientIdForOIDC"
]


# --- restJson1 ser/de ---
def serialize_json(value: ClientIdsForOIDC) -> list:
    return list(value)


def deserialize_json(data: list) -> ClientIdsForOIDC:
    return list(data)
