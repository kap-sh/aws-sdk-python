"""Generated from Smithy shape ``com.amazonaws.appflow#SalesforceDataTransferApi``."""

from typing import Literal, TypeAlias, cast

SalesforceDataTransferApi: TypeAlias = Literal[
    "AUTOMATIC",
    "BULKV2",
    "REST_SYNC",
]


# --- restJson1 ser/de ---
def serialize_json(value: SalesforceDataTransferApi) -> str:
    return value


def deserialize_json(data: str) -> SalesforceDataTransferApi:
    return cast(SalesforceDataTransferApi, data)
