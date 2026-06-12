"""Generated from Smithy shape ``com.amazonaws.apigateway#AccessAssociationSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

AccessAssociationSourceType: TypeAlias = Literal["VPCE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("VPCE",))


def serialize_json(value: AccessAssociationSourceType) -> str:
    return value


def deserialize_json(data: str) -> AccessAssociationSourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AccessAssociationSourceType value: {data!r}"
        )
    return cast(AccessAssociationSourceType, data)
