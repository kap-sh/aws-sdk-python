"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_SUCCESSFUL",
        "CREATE_IN_PROGRESS",
        "CREATE_FAILED",
        "DELETE_SUCCESSFUL",
        "DELETE_FAILED",
        "DELETE_IN_PROGRESS",
        "UPDATE_SUCCESSFUL",
        "UPDATE_IN_PROGRESS",
        "UPDATE_FAILED",
    )
)


def serialize_aws_json_1_1(value: OrganizationResourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OrganizationResourceStatus value: {data!r}"
        )
    return cast(OrganizationResourceStatus, data)
