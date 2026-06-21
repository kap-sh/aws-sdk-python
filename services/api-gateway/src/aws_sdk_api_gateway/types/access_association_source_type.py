"""Generated from Smithy shape ``com.amazonaws.apigateway#AccessAssociationSourceType``."""

from typing import Literal, TypeAlias, cast

AccessAssociationSourceType: TypeAlias = Literal["VPCE",]


# --- restJson1 ser/de ---
def serialize_json(value: AccessAssociationSourceType) -> str:
    return value


def deserialize_json(data: str) -> AccessAssociationSourceType:
    return cast(AccessAssociationSourceType, data)
