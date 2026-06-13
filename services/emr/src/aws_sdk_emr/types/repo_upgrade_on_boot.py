"""Generated from Smithy shape ``com.amazonaws.emr#RepoUpgradeOnBoot``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

RepoUpgradeOnBoot: TypeAlias = Literal[
    "SECURITY",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SECURITY",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: RepoUpgradeOnBoot) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RepoUpgradeOnBoot:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RepoUpgradeOnBoot value: {data!r}")
    return cast(RepoUpgradeOnBoot, data)
