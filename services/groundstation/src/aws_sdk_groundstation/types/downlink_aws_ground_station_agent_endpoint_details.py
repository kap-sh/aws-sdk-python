"""Generated from Smithy shape ``com.amazonaws.groundstation#DownlinkAwsGroundStationAgentEndpointDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.agent_status
    import aws_sdk_groundstation.types.audit_results
    import aws_sdk_groundstation.types.downlink_dataflow_details
    import aws_sdk_groundstation.types.safe_name


class DownlinkAwsGroundStationAgentEndpointDetails(TypedDict):
    name: "aws_sdk_groundstation.types.safe_name.SafeName"
    """<p>Downlink dataflow endpoint name</p>"""
    dataflow_details: (
        "aws_sdk_groundstation.types.downlink_dataflow_details.DownlinkDataflowDetails"
    )
    """<p>Dataflow details for the downlink endpoint</p>"""
    agent_status: NotRequired["aws_sdk_groundstation.types.agent_status.AgentStatus"]
    """<p>Status of the agent associated with the downlink dataflow endpoint</p>"""
    audit_results: NotRequired["aws_sdk_groundstation.types.audit_results.AuditResults"]
    """<p>Health audit results for the downlink dataflow endpoint</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DownlinkAwsGroundStationAgentEndpointDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_groundstation.types.downlink_dataflow_details

    out["dataflowDetails"] = (
        aws_sdk_groundstation.types.downlink_dataflow_details.serialize_json(
            value["dataflow_details"]
        )
    )
    if "agent_status" in value:
        import aws_sdk_groundstation.types.agent_status

        out["agentStatus"] = aws_sdk_groundstation.types.agent_status.serialize_json(
            value["agent_status"]
        )
    if "audit_results" in value:
        import aws_sdk_groundstation.types.audit_results

        out["auditResults"] = aws_sdk_groundstation.types.audit_results.serialize_json(
            value["audit_results"]
        )
    return out


def deserialize_json(data: dict) -> DownlinkAwsGroundStationAgentEndpointDetails:
    out: DownlinkAwsGroundStationAgentEndpointDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "DownlinkAwsGroundStationAgentEndpointDetails.name required"
        )
    if "dataflowDetails" in data:
        import aws_sdk_groundstation.types.downlink_dataflow_details

        out["dataflow_details"] = (
            aws_sdk_groundstation.types.downlink_dataflow_details.deserialize_json(
                data["dataflowDetails"]
            )
        )
    else:
        raise DeserializationError(
            "DownlinkAwsGroundStationAgentEndpointDetails.dataflow_details required"
        )
    if "agentStatus" in data:
        import aws_sdk_groundstation.types.agent_status

        out["agent_status"] = aws_sdk_groundstation.types.agent_status.deserialize_json(
            data["agentStatus"]
        )
    if "auditResults" in data:
        import aws_sdk_groundstation.types.audit_results

        out["audit_results"] = (
            aws_sdk_groundstation.types.audit_results.deserialize_json(
                data["auditResults"]
            )
        )
    return out
