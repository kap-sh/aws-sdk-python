"""Generated from Smithy shape ``com.amazonaws.datasync#ManifestAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

ManifestAction: TypeAlias = Literal["TRANSFER",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TRANSFER",))


def serialize_aws_json_1_1(value: ManifestAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManifestAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManifestAction value: {data!r}")
    return cast(ManifestAction, data)
