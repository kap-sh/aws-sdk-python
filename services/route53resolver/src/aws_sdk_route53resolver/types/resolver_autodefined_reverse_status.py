"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverAutodefinedReverseStatus``."""

from typing import Literal, TypeAlias, cast

ResolverAutodefinedReverseStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "DISABLED",
    "UPDATING_TO_USE_LOCAL_RESOURCE_SETTING",
    "USE_LOCAL_RESOURCE_SETTING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverAutodefinedReverseStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolverAutodefinedReverseStatus:
    return cast(ResolverAutodefinedReverseStatus, data)
