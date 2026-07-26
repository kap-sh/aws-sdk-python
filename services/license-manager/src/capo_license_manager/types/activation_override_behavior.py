"""Generated from Smithy shape ``com.amazonaws.licensemanager#ActivationOverrideBehavior``."""

from typing import Literal, TypeAlias, cast

ActivationOverrideBehavior: TypeAlias = Literal[
    "DISTRIBUTED_GRANTS_ONLY",
    "ALL_GRANTS_PERMITTED_BY_ISSUER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActivationOverrideBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActivationOverrideBehavior:
    return cast(ActivationOverrideBehavior, data)
