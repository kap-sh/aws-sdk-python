"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationResourceDetailedStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

OrganizationResourceDetailedStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: OrganizationResourceDetailedStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationResourceDetailedStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OrganizationResourceDetailedStatus value: {data!r}"
        )
    return cast(OrganizationResourceDetailedStatus, data)
