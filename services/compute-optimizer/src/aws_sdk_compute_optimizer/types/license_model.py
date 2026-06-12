"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LicenseModel: TypeAlias = Literal[
    "LicenseIncluded",
    "BringYourOwnLicense",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LicenseIncluded",
        "BringYourOwnLicense",
    )
)


def serialize_aws_json_1_0(value: LicenseModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LicenseModel value: {data!r}")
    return cast(LicenseModel, data)
