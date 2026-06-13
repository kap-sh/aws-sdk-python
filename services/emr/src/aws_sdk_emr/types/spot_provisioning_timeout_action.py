"""Generated from Smithy shape ``com.amazonaws.emr#SpotProvisioningTimeoutAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

SpotProvisioningTimeoutAction: TypeAlias = Literal[
    "SWITCH_TO_ON_DEMAND",
    "TERMINATE_CLUSTER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SWITCH_TO_ON_DEMAND",
        "TERMINATE_CLUSTER",
    )
)


def serialize_aws_json_1_1(value: SpotProvisioningTimeoutAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SpotProvisioningTimeoutAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SpotProvisioningTimeoutAction value: {data!r}"
        )
    return cast(SpotProvisioningTimeoutAction, data)
