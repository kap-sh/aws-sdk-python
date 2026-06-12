"""Generated from Smithy shape ``com.amazonaws.transfer#MdnSigningAlg``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

MdnSigningAlg: TypeAlias = Literal[
    "SHA256",
    "SHA384",
    "SHA512",
    "SHA1",
    "NONE",
    "DEFAULT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHA256",
        "SHA384",
        "SHA512",
        "SHA1",
        "NONE",
        "DEFAULT",
    )
)


def serialize_aws_json_1_1(value: MdnSigningAlg) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MdnSigningAlg:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MdnSigningAlg value: {data!r}")
    return cast(MdnSigningAlg, data)
