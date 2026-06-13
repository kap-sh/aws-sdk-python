"""Generated from Smithy shape ``com.amazonaws.odb#LicenseModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

LicenseModel: TypeAlias = Literal[
    "BRING_YOUR_OWN_LICENSE",
    "LICENSE_INCLUDED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BRING_YOUR_OWN_LICENSE",
        "LICENSE_INCLUDED",
    )
)


def serialize_aws_json_1_0(value: LicenseModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LicenseModel value: {data!r}")
    return cast(LicenseModel, data)
