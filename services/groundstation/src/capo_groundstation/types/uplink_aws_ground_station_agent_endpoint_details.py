"""Generated from Smithy shape ``com.amazonaws.groundstation#UplinkAwsGroundStationAgentEndpointDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.agent_status
    import capo_groundstation.types.audit_results
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.uplink_dataflow_details


class UplinkAwsGroundStationAgentEndpointDetails(TypedDict, closed=True):
    name: "capo_groundstation.types.safe_name.SafeName"
    """<p>Uplink dataflow endpoint name</p>"""
    dataflow_details: (
        "capo_groundstation.types.uplink_dataflow_details.UplinkDataflowDetails"
    )
    """<p>Dataflow details for the uplink endpoint</p>"""
    agent_status: NotRequired["capo_groundstation.types.agent_status.AgentStatus"]
    """<p>Status of the agent associated with the uplink dataflow endpoint</p>"""
    audit_results: NotRequired["capo_groundstation.types.audit_results.AuditResults"]
    """<p>Health audit results for the uplink dataflow endpoint</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UplinkAwsGroundStationAgentEndpointDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_groundstation.types.uplink_dataflow_details

    out["dataflowDetails"] = (
        capo_groundstation.types.uplink_dataflow_details.serialize_json(
            value["dataflow_details"]
        )
    )
    if "agent_status" in value:
        import capo_groundstation.types.agent_status

        out["agentStatus"] = capo_groundstation.types.agent_status.serialize_json(
            value["agent_status"]
        )
    if "audit_results" in value:
        import capo_groundstation.types.audit_results

        out["auditResults"] = capo_groundstation.types.audit_results.serialize_json(
            value["audit_results"]
        )
    return out


def deserialize_json(data: dict) -> UplinkAwsGroundStationAgentEndpointDetails:
    out: UplinkAwsGroundStationAgentEndpointDetails = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "UplinkAwsGroundStationAgentEndpointDetails.name required"
        )
    if "dataflowDetails" in data:
        import capo_groundstation.types.uplink_dataflow_details

        out["dataflow_details"] = (
            capo_groundstation.types.uplink_dataflow_details.deserialize_json(
                data["dataflowDetails"]
            )
        )
    else:
        raise DeserializationError(
            "UplinkAwsGroundStationAgentEndpointDetails.dataflow_details required"
        )
    if "agentStatus" in data:
        import capo_groundstation.types.agent_status

        out["agent_status"] = capo_groundstation.types.agent_status.deserialize_json(
            data["agentStatus"]
        )
    if "auditResults" in data:
        import capo_groundstation.types.audit_results

        out["audit_results"] = capo_groundstation.types.audit_results.deserialize_json(
            data["auditResults"]
        )
    return out
