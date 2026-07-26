"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ConfiguredAudienceModelStatus``."""

from typing import Literal, TypeAlias, cast

ConfiguredAudienceModelStatus: TypeAlias = Literal["ACTIVE",]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredAudienceModelStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfiguredAudienceModelStatus:
    return cast(ConfiguredAudienceModelStatus, data)
