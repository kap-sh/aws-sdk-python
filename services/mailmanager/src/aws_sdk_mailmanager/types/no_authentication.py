"""Generated from Smithy shape ``com.amazonaws.mailmanager#NoAuthentication``."""

from typing import TypedDict


class NoAuthentication(TypedDict):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NoAuthentication) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> NoAuthentication:
    out: NoAuthentication = {}  # type: ignore[typeddict-item]
    return out
