"""Generated from Smithy shape ``com.amazonaws.appflow#SalesforceDataTransferApi``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

SalesforceDataTransferApi: TypeAlias = Literal[
    "AUTOMATIC",
    "BULKV2",
    "REST_SYNC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "BULKV2",
        "REST_SYNC",
    )
)


def serialize_json(value: SalesforceDataTransferApi) -> str:
    return value


def deserialize_json(data: str) -> SalesforceDataTransferApi:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SalesforceDataTransferApi value: {data!r}")
    return cast(SalesforceDataTransferApi, data)
