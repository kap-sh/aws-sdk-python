"""Generated from Smithy shape ``com.amazonaws.mailmanager#NoAuthentication``."""

from typing_extensions import TypedDict


class NoAuthentication(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NoAuthentication) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> NoAuthentication:
    out: NoAuthentication = {}  # type: ignore[typeddict-item]
    return out
