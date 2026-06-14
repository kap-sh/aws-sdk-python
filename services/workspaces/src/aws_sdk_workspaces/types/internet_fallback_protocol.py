"""Generated from Smithy shape ``com.amazonaws.workspaces#InternetFallbackProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

InternetFallbackProtocol: TypeAlias = Literal["PCOIP",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PCOIP",))


def serialize_aws_json_1_1(value: InternetFallbackProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InternetFallbackProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InternetFallbackProtocol value: {data!r}")
    return cast(InternetFallbackProtocol, data)
