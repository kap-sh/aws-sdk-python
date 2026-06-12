"""Generated from Smithy shape ``com.amazonaws.datasync#ManifestFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

ManifestFormat: TypeAlias = Literal["CSV",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CSV",))


def serialize_aws_json_1_1(value: ManifestFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManifestFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManifestFormat value: {data!r}")
    return cast(ManifestFormat, data)
