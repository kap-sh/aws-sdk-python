"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerClaimStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

GameServerClaimStatus: TypeAlias = Literal["CLAIMED",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CLAIMED",))


def serialize_aws_json_1_1(value: GameServerClaimStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GameServerClaimStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GameServerClaimStatus value: {data!r}")
    return cast(GameServerClaimStatus, data)
