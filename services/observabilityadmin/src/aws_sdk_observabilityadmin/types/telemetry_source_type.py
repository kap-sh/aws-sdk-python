"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetrySourceType``."""

from typing import Literal, TypeAlias, cast

"""<p> Specifies the type of telemetry source for a resource, such as EKS cluster logs. </p>"""
TelemetrySourceType: TypeAlias = Literal[
    "VPC_FLOW_LOGS",
    "ROUTE53_RESOLVER_QUERY_LOGS",
    "EKS_AUDIT_LOGS",
    "EKS_AUTHENTICATOR_LOGS",
    "EKS_CONTROLLER_MANAGER_LOGS",
    "EKS_SCHEDULER_LOGS",
    "EKS_API_LOGS",
]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetrySourceType) -> str:
    return value


def deserialize_json(data: str) -> TelemetrySourceType:
    return cast(TelemetrySourceType, data)
