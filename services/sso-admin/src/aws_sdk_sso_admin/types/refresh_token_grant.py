"""Generated from Smithy shape ``com.amazonaws.ssoadmin#RefreshTokenGrant``."""

from typing_extensions import TypedDict


class RefreshTokenGrant(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshTokenGrant) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RefreshTokenGrant:
    out: RefreshTokenGrant = {}  # type: ignore[typeddict-item]
    return out
