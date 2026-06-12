"""Generated from Smithy shape ``com.amazonaws.directoryservice#RadiusAuthenticationProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

RadiusAuthenticationProtocol: TypeAlias = Literal[
    "PAP",
    "CHAP",
    "MS-CHAPv1",
    "MS-CHAPv2",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PAP",
        "CHAP",
        "MS-CHAPv1",
        "MS-CHAPv2",
    )
)


def serialize_aws_json_1_1(value: RadiusAuthenticationProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RadiusAuthenticationProtocol:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RadiusAuthenticationProtocol value: {data!r}"
        )
    return cast(RadiusAuthenticationProtocol, data)
