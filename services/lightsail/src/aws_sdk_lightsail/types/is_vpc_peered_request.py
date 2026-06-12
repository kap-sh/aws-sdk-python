"""Generated from Smithy shape ``com.amazonaws.lightsail#IsVpcPeeredRequest``."""

from typing import TypedDict


class IsVpcPeeredRequest(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IsVpcPeeredRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> IsVpcPeeredRequest:
    out: IsVpcPeeredRequest = {}  # type: ignore[typeddict-item]
    return out
