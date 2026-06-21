"""Generated from Smithy shape ``com.amazonaws.emr#RepoUpgradeOnBoot``."""

from typing import Literal, TypeAlias, cast

RepoUpgradeOnBoot: TypeAlias = Literal[
    "SECURITY",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepoUpgradeOnBoot) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RepoUpgradeOnBoot:
    return cast(RepoUpgradeOnBoot, data)
