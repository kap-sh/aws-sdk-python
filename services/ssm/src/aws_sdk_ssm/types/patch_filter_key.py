"""Generated from Smithy shape ``com.amazonaws.ssm#PatchFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

PatchFilterKey: TypeAlias = Literal[
    "ARCH",
    "ADVISORY_ID",
    "BUGZILLA_ID",
    "PATCH_SET",
    "PRODUCT",
    "PRODUCT_FAMILY",
    "CLASSIFICATION",
    "CVE_ID",
    "EPOCH",
    "MSRC_SEVERITY",
    "NAME",
    "PATCH_ID",
    "SECTION",
    "PRIORITY",
    "REPOSITORY",
    "RELEASE",
    "SEVERITY",
    "SECURITY",
    "VERSION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ARCH",
        "ADVISORY_ID",
        "BUGZILLA_ID",
        "PATCH_SET",
        "PRODUCT",
        "PRODUCT_FAMILY",
        "CLASSIFICATION",
        "CVE_ID",
        "EPOCH",
        "MSRC_SEVERITY",
        "NAME",
        "PATCH_ID",
        "SECTION",
        "PRIORITY",
        "REPOSITORY",
        "RELEASE",
        "SEVERITY",
        "SECURITY",
        "VERSION",
    )
)


def serialize_aws_json_1_1(value: PatchFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PatchFilterKey value: {data!r}")
    return cast(PatchFilterKey, data)
