"""Generated from Smithy shape ``com.amazonaws.fms#ThirdPartyFirewallAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

ThirdPartyFirewallAssociationStatus: TypeAlias = Literal[
    "ONBOARDING",
    "ONBOARD_COMPLETE",
    "OFFBOARDING",
    "OFFBOARD_COMPLETE",
    "NOT_EXIST",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONBOARDING",
        "ONBOARD_COMPLETE",
        "OFFBOARDING",
        "OFFBOARD_COMPLETE",
        "NOT_EXIST",
    )
)


def serialize_aws_json_1_1(value: ThirdPartyFirewallAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThirdPartyFirewallAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ThirdPartyFirewallAssociationStatus value: {data!r}"
        )
    return cast(ThirdPartyFirewallAssociationStatus, data)
