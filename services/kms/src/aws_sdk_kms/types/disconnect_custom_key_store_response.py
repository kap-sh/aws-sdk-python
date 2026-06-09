"""Generated from Smithy shape ``com.amazonaws.kms#DisconnectCustomKeyStoreResponse``."""

from typing import TypedDict


class DisconnectCustomKeyStoreResponse(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisconnectCustomKeyStoreResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisconnectCustomKeyStoreResponse:
    out: DisconnectCustomKeyStoreResponse = {}  # type: ignore[typeddict-item]
    return out
