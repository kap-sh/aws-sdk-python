"""Generated from Smithy shape ``com.amazonaws.route53resolver#OutpostResolverStatus``."""

from typing import Literal, TypeAlias, cast

OutpostResolverStatus: TypeAlias = Literal[
    "CREATING",
    "OPERATIONAL",
    "UPDATING",
    "DELETING",
    "ACTION_NEEDED",
    "FAILED_CREATION",
    "FAILED_DELETION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutpostResolverStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OutpostResolverStatus:
    return cast(OutpostResolverStatus, data)
