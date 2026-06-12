"""Generated from Smithy shape ``com.amazonaws.codedeploy#GreenFleetProvisioningAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

GreenFleetProvisioningAction: TypeAlias = Literal[
    "DISCOVER_EXISTING",
    "COPY_AUTO_SCALING_GROUP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISCOVER_EXISTING",
        "COPY_AUTO_SCALING_GROUP",
    )
)


def serialize_aws_json_1_1(value: GreenFleetProvisioningAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GreenFleetProvisioningAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GreenFleetProvisioningAction value: {data!r}"
        )
    return cast(GreenFleetProvisioningAction, data)
