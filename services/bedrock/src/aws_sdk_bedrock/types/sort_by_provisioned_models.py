"""Generated from Smithy shape ``com.amazonaws.bedrock#SortByProvisionedModels``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

SortByProvisionedModels: TypeAlias = Literal["CreationTime",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CreationTime",))


def serialize_json(value: SortByProvisionedModels) -> str:
    return value


def deserialize_json(data: str) -> SortByProvisionedModels:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortByProvisionedModels value: {data!r}")
    return cast(SortByProvisionedModels, data)
