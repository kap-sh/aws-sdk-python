"""Generated from Smithy shape ``com.amazonaws.configservice#DeliveryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

DeliveryStatus: TypeAlias = Literal[
    "Success",
    "Failure",
    "Not_Applicable",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Success",
        "Failure",
        "Not_Applicable",
    )
)


def serialize_aws_json_1_1(value: DeliveryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeliveryStatus value: {data!r}")
    return cast(DeliveryStatus, data)
