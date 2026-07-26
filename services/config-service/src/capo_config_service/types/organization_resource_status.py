"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationResourceStatus``."""

from typing import Literal, TypeAlias, cast

OrganizationResourceStatus: TypeAlias = Literal[
    "CREATE_SUCCESSFUL",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "DELETE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationResourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationResourceStatus:
    return cast(OrganizationResourceStatus, data)
