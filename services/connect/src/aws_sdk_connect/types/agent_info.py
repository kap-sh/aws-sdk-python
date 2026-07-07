"""Generated from Smithy shape ``com.amazonaws.connect#AgentInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_pause_duration_in_seconds
    import aws_sdk_connect.types.agent_resource_id
    import aws_sdk_connect.types.device_info
    import aws_sdk_connect.types.duration
    import aws_sdk_connect.types.hierarchy_groups
    import aws_sdk_connect.types.participant_capabilities
    import aws_sdk_connect.types.state_transitions
    import aws_sdk_connect.types.timestamp
    import aws_sdk_connect.types.voice_enhancement_mode


class AgentInfo(TypedDict, closed=True):
    id: NotRequired["aws_sdk_connect.types.agent_resource_id.AgentResourceId"]
    """<p>The identifier of the agent who accepted the contact.</p>"""
    accepted_by_agent_timestamp: NotRequired[
        "aws_sdk_connect.types.timestamp.Timestamp"
    ]
    """<p>The timestamp when the contact was accepted by the agent.</p>"""
    preview_end_timestamp: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the agent finished previewing the contact.</p>"""
    connected_to_agent_timestamp: NotRequired[
        "aws_sdk_connect.types.timestamp.Timestamp"
    ]
    """<p>The timestamp when the contact was connected to the agent.</p>"""
    agent_pause_duration_in_seconds: NotRequired[
        "aws_sdk_connect.types.agent_pause_duration_in_seconds.AgentPauseDurationInSeconds"
    ]
    """<p>Agent pause duration for a contact in seconds.</p>"""
    hierarchy_groups: NotRequired[
        "aws_sdk_connect.types.hierarchy_groups.HierarchyGroups"
    ]
    """<p>The agent hierarchy groups for the agent.</p>"""
    device_info: NotRequired["aws_sdk_connect.types.device_info.DeviceInfo"]
    """<p>Information regarding Agent’s device.</p>"""
    capabilities: NotRequired[
        "aws_sdk_connect.types.participant_capabilities.ParticipantCapabilities"
    ]
    after_contact_work_duration: NotRequired["aws_sdk_connect.types.duration.Duration"]
    """<p>The difference in time, in whole seconds, between <code>AfterContactWorkStartTimestamp</code> and <code>AfterContactWorkEndTimestamp</code>.</p>"""
    after_contact_work_start_timestamp: NotRequired[
        "aws_sdk_connect.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the agent started doing After Contact Work for the contact, in UTC time.</p>"""
    after_contact_work_end_timestamp: NotRequired[
        "aws_sdk_connect.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the agent ended After Contact Work for the contact, in UTC time. In cases when agent finishes doing <code>AfterContactWork</code> for chat contacts and switches their activity status to offline or equivalent without clearing the contact in CCP, discrepancies may be noticed for <code>AfterContactWorkEndTimestamp</code>.</p>"""
    agent_initiated_hold_duration: NotRequired[
        "aws_sdk_connect.types.duration.Duration"
    ]
    """<p>The total hold duration in seconds initiated by the agent.</p>"""
    state_transitions: NotRequired[
        "aws_sdk_connect.types.state_transitions.StateTransitions"
    ]
    """<p>List of <code>StateTransition</code> for a supervisor.</p>"""
    voice_enhancement_mode: NotRequired[
        "aws_sdk_connect.types.voice_enhancement_mode.VoiceEnhancementMode"
    ]
    """<p>The voice enhancement mode used by the agent as the call is ending. Valid values: VOICE_ISOLATION | NOISE_SUPPRESSION | NONE. A value of null indicates this mode has not yet been set for this user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentInfo) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "accepted_by_agent_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["AcceptedByAgentTimestamp"] = (
            aws_sdk_connect.types.timestamp.serialize_json(
                value["accepted_by_agent_timestamp"]
            )
        )
    if "preview_end_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["PreviewEndTimestamp"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["preview_end_timestamp"]
        )
    if "connected_to_agent_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["ConnectedToAgentTimestamp"] = (
            aws_sdk_connect.types.timestamp.serialize_json(
                value["connected_to_agent_timestamp"]
            )
        )
    if "agent_pause_duration_in_seconds" in value:
        out["AgentPauseDurationInSeconds"] = value["agent_pause_duration_in_seconds"]
    if "hierarchy_groups" in value:
        import aws_sdk_connect.types.hierarchy_groups

        out["HierarchyGroups"] = aws_sdk_connect.types.hierarchy_groups.serialize_json(
            value["hierarchy_groups"]
        )
    if "device_info" in value:
        import aws_sdk_connect.types.device_info

        out["DeviceInfo"] = aws_sdk_connect.types.device_info.serialize_json(
            value["device_info"]
        )
    if "capabilities" in value:
        import aws_sdk_connect.types.participant_capabilities

        out["Capabilities"] = (
            aws_sdk_connect.types.participant_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    if "after_contact_work_duration" in value:
        out["AfterContactWorkDuration"] = value["after_contact_work_duration"]
    if "after_contact_work_start_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["AfterContactWorkStartTimestamp"] = (
            aws_sdk_connect.types.timestamp.serialize_json(
                value["after_contact_work_start_timestamp"]
            )
        )
    if "after_contact_work_end_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["AfterContactWorkEndTimestamp"] = (
            aws_sdk_connect.types.timestamp.serialize_json(
                value["after_contact_work_end_timestamp"]
            )
        )
    if "agent_initiated_hold_duration" in value:
        out["AgentInitiatedHoldDuration"] = value["agent_initiated_hold_duration"]
    if "state_transitions" in value:
        import aws_sdk_connect.types.state_transitions

        out["StateTransitions"] = (
            aws_sdk_connect.types.state_transitions.serialize_json(
                value["state_transitions"]
            )
        )
    if "voice_enhancement_mode" in value:
        import aws_sdk_connect.types.voice_enhancement_mode

        out["VoiceEnhancementMode"] = (
            aws_sdk_connect.types.voice_enhancement_mode.serialize_json(
                value["voice_enhancement_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentInfo:
    out: AgentInfo = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "AcceptedByAgentTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["accepted_by_agent_timestamp"] = (
            aws_sdk_connect.types.timestamp.deserialize_json(
                data["AcceptedByAgentTimestamp"]
            )
        )
    if "PreviewEndTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["preview_end_timestamp"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["PreviewEndTimestamp"]
        )
    if "ConnectedToAgentTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["connected_to_agent_timestamp"] = (
            aws_sdk_connect.types.timestamp.deserialize_json(
                data["ConnectedToAgentTimestamp"]
            )
        )
    if "AgentPauseDurationInSeconds" in data:
        out["agent_pause_duration_in_seconds"] = data["AgentPauseDurationInSeconds"]
    if "HierarchyGroups" in data:
        import aws_sdk_connect.types.hierarchy_groups

        out["hierarchy_groups"] = (
            aws_sdk_connect.types.hierarchy_groups.deserialize_json(
                data["HierarchyGroups"]
            )
        )
    if "DeviceInfo" in data:
        import aws_sdk_connect.types.device_info

        out["device_info"] = aws_sdk_connect.types.device_info.deserialize_json(
            data["DeviceInfo"]
        )
    if "Capabilities" in data:
        import aws_sdk_connect.types.participant_capabilities

        out["capabilities"] = (
            aws_sdk_connect.types.participant_capabilities.deserialize_json(
                data["Capabilities"]
            )
        )
    if "AfterContactWorkDuration" in data:
        out["after_contact_work_duration"] = data["AfterContactWorkDuration"]
    if "AfterContactWorkStartTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["after_contact_work_start_timestamp"] = (
            aws_sdk_connect.types.timestamp.deserialize_json(
                data["AfterContactWorkStartTimestamp"]
            )
        )
    if "AfterContactWorkEndTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["after_contact_work_end_timestamp"] = (
            aws_sdk_connect.types.timestamp.deserialize_json(
                data["AfterContactWorkEndTimestamp"]
            )
        )
    if "AgentInitiatedHoldDuration" in data:
        out["agent_initiated_hold_duration"] = data["AgentInitiatedHoldDuration"]
    if "StateTransitions" in data:
        import aws_sdk_connect.types.state_transitions

        out["state_transitions"] = (
            aws_sdk_connect.types.state_transitions.deserialize_json(
                data["StateTransitions"]
            )
        )
    if "VoiceEnhancementMode" in data:
        import aws_sdk_connect.types.voice_enhancement_mode

        out["voice_enhancement_mode"] = (
            aws_sdk_connect.types.voice_enhancement_mode.deserialize_json(
                data["VoiceEnhancementMode"]
            )
        )
    return out
