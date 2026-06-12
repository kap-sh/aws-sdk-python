"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationRuleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

OrganizationRuleStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: OrganizationRuleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationRuleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrganizationRuleStatus value: {data!r}")
    return cast(OrganizationRuleStatus, data)
