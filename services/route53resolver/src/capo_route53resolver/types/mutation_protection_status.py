"""Generated from Smithy shape ``com.amazonaws.route53resolver#MutationProtectionStatus``."""

from typing import Literal, TypeAlias, cast

MutationProtectionStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MutationProtectionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MutationProtectionStatus:
    return cast(MutationProtectionStatus, data)
