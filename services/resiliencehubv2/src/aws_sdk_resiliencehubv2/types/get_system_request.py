"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetSystemRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn


class GetSystemRequest(TypedDict):
    system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: GetSystemRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSystemRequest:
    out: GetSystemRequest = {}  # type: ignore[typeddict-item]
    return out
