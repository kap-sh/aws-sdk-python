"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.application_id
    import capo_securityagent.types.membership_config
    import capo_securityagent.types.membership_id
    import capo_securityagent.types.membership_type


class CreateMembershipRequest(TypedDict, closed=True):
    application_id: "capo_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the application that contains the agent space.</p>"""
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space to grant access to.</p>"""
    membership_id: "capo_securityagent.types.membership_id.MembershipId"
    """<p>The unique identifier for the membership.</p>"""
    member_type: "capo_securityagent.types.membership_type.MembershipType"
    """<p>The type of member. Currently, only USER is supported.</p>"""
    config: NotRequired["capo_securityagent.types.membership_config.MembershipConfig"]
    """<p>The configuration for the membership, such as the user role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembershipRequest) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    out["membershipId"] = value["membership_id"]
    import capo_securityagent.types.membership_type

    out["memberType"] = capo_securityagent.types.membership_type.serialize_json(
        value["member_type"]
    )
    if "config" in value:
        import capo_securityagent.types.membership_config

        out["config"] = capo_securityagent.types.membership_config.serialize_json(
            value["config"]
        )
    return out


def deserialize_json(data: dict) -> CreateMembershipRequest:
    out: CreateMembershipRequest = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("CreateMembershipRequest.application_id required")
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("CreateMembershipRequest.agent_space_id required")
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("CreateMembershipRequest.membership_id required")
    if "memberType" in data:
        import capo_securityagent.types.membership_type

        out["member_type"] = capo_securityagent.types.membership_type.deserialize_json(
            data["memberType"]
        )
    else:
        raise DeserializationError("CreateMembershipRequest.member_type required")
    if "config" in data:
        import capo_securityagent.types.membership_config

        out["config"] = capo_securityagent.types.membership_config.deserialize_json(
            data["config"]
        )
    return out
