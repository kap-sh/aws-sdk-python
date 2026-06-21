"""Generated from Smithy shape ``com.amazonaws.workspaces#ApplicationAssociatedResourceType``."""

from typing import Literal, TypeAlias, cast

ApplicationAssociatedResourceType: TypeAlias = Literal[
    "WORKSPACE",
    "BUNDLE",
    "IMAGE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationAssociatedResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationAssociatedResourceType:
    return cast(ApplicationAssociatedResourceType, data)
