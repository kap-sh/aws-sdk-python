"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteAnalysisCompletionReasonCode``."""

from typing import Literal, TypeAlias, cast

RouteAnalysisCompletionReasonCode: TypeAlias = Literal[
    "TRANSIT_GATEWAY_ATTACHMENT_NOT_FOUND",
    "TRANSIT_GATEWAY_ATTACHMENT_NOT_IN_TRANSIT_GATEWAY",
    "CYCLIC_PATH_DETECTED",
    "TRANSIT_GATEWAY_ATTACHMENT_STABLE_ROUTE_TABLE_NOT_FOUND",
    "ROUTE_NOT_FOUND",
    "BLACKHOLE_ROUTE_FOR_DESTINATION_FOUND",
    "INACTIVE_ROUTE_FOR_DESTINATION_FOUND",
    "TRANSIT_GATEWAY_ATTACHMENT_ATTACH_ARN_NO_MATCH",
    "MAX_HOPS_EXCEEDED",
    "POSSIBLE_MIDDLEBOX",
    "NO_DESTINATION_ARN_PROVIDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAnalysisCompletionReasonCode) -> str:
    return value


def deserialize_json(data: str) -> RouteAnalysisCompletionReasonCode:
    return cast(RouteAnalysisCompletionReasonCode, data)
