"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.capability_report_version
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoints
    import aws_sdk_iot_managed_integrations.types.node_id


class MatterCapabilityReport(TypedDict, closed=True):
    version: "aws_sdk_iot_managed_integrations.types.capability_report_version.CapabilityReportVersion"
    """<p>The version of the capability report.</p>"""
    node_id: NotRequired["aws_sdk_iot_managed_integrations.types.node_id.NodeId"]
    """<p>The numeric identifier of the node.</p>"""
    endpoints: "aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoints.MatterCapabilityReportEndpoints"
    """<p>The endpoints used in the capability report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReport) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    if "node_id" in value:
        out["nodeId"] = value["node_id"]
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoints

    out["endpoints"] = (
        aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoints.serialize_json(
            value["endpoints"]
        )
    )
    return out


def deserialize_json(data: dict) -> MatterCapabilityReport:
    out: MatterCapabilityReport = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("MatterCapabilityReport.version required")
    if "nodeId" in data:
        out["node_id"] = data["nodeId"]
    if "endpoints" in data:
        import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoints

        out["endpoints"] = (
            aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoints.deserialize_json(
                data["endpoints"]
            )
        )
    else:
        raise DeserializationError("MatterCapabilityReport.endpoints required")
    return out
