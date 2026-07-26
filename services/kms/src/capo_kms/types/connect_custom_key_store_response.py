"""Generated from Smithy shape ``com.amazonaws.kms#ConnectCustomKeyStoreResponse``."""

from typing_extensions import TypedDict


class ConnectCustomKeyStoreResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectCustomKeyStoreResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectCustomKeyStoreResponse:
    out: ConnectCustomKeyStoreResponse = {}  # type: ignore[typeddict-item]
    return out
