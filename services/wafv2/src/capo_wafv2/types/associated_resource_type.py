"""Generated from Smithy shape ``com.amazonaws.wafv2#AssociatedResourceType``."""

from typing import Literal, TypeAlias, cast

AssociatedResourceType: TypeAlias = Literal[
    "CLOUDFRONT",
    "API_GATEWAY",
    "COGNITO_USER_POOL",
    "APP_RUNNER_SERVICE",
    "VERIFIED_ACCESS_INSTANCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociatedResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociatedResourceType:
    return cast(AssociatedResourceType, data)
