"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ResaleAccountModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

ResaleAccountModel: TypeAlias = Literal[
    "DISTRIBUTOR",
    "END_CUSTOMER",
    "SOLUTION_PROVIDER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISTRIBUTOR",
        "END_CUSTOMER",
        "SOLUTION_PROVIDER",
    )
)


def serialize_aws_json_1_0(value: ResaleAccountModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResaleAccountModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResaleAccountModel value: {data!r}")
    return cast(ResaleAccountModel, data)
