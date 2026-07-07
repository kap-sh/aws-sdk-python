"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#CustomerConnectorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.integer


class CustomerConnectorInfo(TypedDict, closed=True):
    active_connectors: "aws_sdk_application_discovery_service.types.integer.Integer"
    """<p>Number of active discovery connectors.</p>"""
    healthy_connectors: "aws_sdk_application_discovery_service.types.integer.Integer"
    """<p>Number of healthy discovery connectors.</p>"""
    black_listed_connectors: (
        "aws_sdk_application_discovery_service.types.integer.Integer"
    )
    """<p>Number of blacklisted discovery connectors.</p>"""
    shutdown_connectors: "aws_sdk_application_discovery_service.types.integer.Integer"
    """<p>Number of discovery connectors with status SHUTDOWN,</p>"""
    unhealthy_connectors: "aws_sdk_application_discovery_service.types.integer.Integer"
    """<p>Number of unhealthy discovery connectors.</p>"""
    total_connectors: "aws_sdk_application_discovery_service.types.integer.Integer"
    """<p>Total number of discovery connectors.</p>"""
    unknown_connectors: "aws_sdk_application_discovery_service.types.integer.Integer"
    """<p>Number of unknown discovery connectors.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerConnectorInfo) -> dict:
    out: dict = {}
    out["activeConnectors"] = value.get("active_connectors", 0)
    out["healthyConnectors"] = value.get("healthy_connectors", 0)
    out["blackListedConnectors"] = value.get("black_listed_connectors", 0)
    out["shutdownConnectors"] = value.get("shutdown_connectors", 0)
    out["unhealthyConnectors"] = value.get("unhealthy_connectors", 0)
    out["totalConnectors"] = value.get("total_connectors", 0)
    out["unknownConnectors"] = value.get("unknown_connectors", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerConnectorInfo:
    out: CustomerConnectorInfo = {}  # type: ignore[typeddict-item]
    if "activeConnectors" in data:
        out["active_connectors"] = data["activeConnectors"]
    else:
        out["active_connectors"] = 0
    if "healthyConnectors" in data:
        out["healthy_connectors"] = data["healthyConnectors"]
    else:
        out["healthy_connectors"] = 0
    if "blackListedConnectors" in data:
        out["black_listed_connectors"] = data["blackListedConnectors"]
    else:
        out["black_listed_connectors"] = 0
    if "shutdownConnectors" in data:
        out["shutdown_connectors"] = data["shutdownConnectors"]
    else:
        out["shutdown_connectors"] = 0
    if "unhealthyConnectors" in data:
        out["unhealthy_connectors"] = data["unhealthyConnectors"]
    else:
        out["unhealthy_connectors"] = 0
    if "totalConnectors" in data:
        out["total_connectors"] = data["totalConnectors"]
    else:
        out["total_connectors"] = 0
    if "unknownConnectors" in data:
        out["unknown_connectors"] = data["unknownConnectors"]
    else:
        out["unknown_connectors"] = 0
    return out
