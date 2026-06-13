"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ConfiguredAudienceModelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

ConfiguredAudienceModelStatus: TypeAlias = Literal["ACTIVE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ACTIVE",))


def serialize_json(value: ConfiguredAudienceModelStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfiguredAudienceModelStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConfiguredAudienceModelStatus value: {data!r}"
        )
    return cast(ConfiguredAudienceModelStatus, data)
