"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetServiceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn


class GetServiceRequest(TypedDict):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServiceRequest:
    out: GetServiceRequest = {}  # type: ignore[typeddict-item]
    return out
