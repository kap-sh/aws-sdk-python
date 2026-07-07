"""Generated from Smithy shape ``com.amazonaws.securityagent#MembershipSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_securityagent.types.agent_space_id
    import aws_sdk_securityagent.types.application_id
    import aws_sdk_securityagent.types.member_metadata
    import aws_sdk_securityagent.types.membership_config
    import aws_sdk_securityagent.types.membership_id
    import aws_sdk_securityagent.types.membership_type


class MembershipSummary(TypedDict, closed=True):
    membership_id: "aws_sdk_securityagent.types.membership_id.MembershipId"
    """<p>The unique identifier of the membership.</p>"""
    application_id: "aws_sdk_securityagent.types.application_id.ApplicationId"
    """<p>The unique identifier of the application.</p>"""
    agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space.</p>"""
    member_type: "aws_sdk_securityagent.types.membership_type.MembershipType"
    """<p>The type of member.</p>"""
    config: NotRequired[
        "aws_sdk_securityagent.types.membership_config.MembershipConfig"
    ]
    """<p>The configuration for the membership.</p>"""
    metadata: NotRequired["aws_sdk_securityagent.types.member_metadata.MemberMetadata"]
    """<p>The metadata for the member.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the membership was created, in UTC format.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time the membership was last updated, in UTC format.</p>"""
    created_by: "str"
    """<p>The identifier of the entity that created the membership.</p>"""
    updated_by: "str"
    """<p>The identifier of the entity that last updated the membership.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MembershipSummary) -> dict:
    out: dict = {}
    out["membershipId"] = value["membership_id"]
    out["applicationId"] = value["application_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    import aws_sdk_securityagent.types.membership_type

    out["memberType"] = aws_sdk_securityagent.types.membership_type.serialize_json(
        value["member_type"]
    )
    if "config" in value:
        import aws_sdk_securityagent.types.membership_config

        out["config"] = aws_sdk_securityagent.types.membership_config.serialize_json(
            value["config"]
        )
    if "metadata" in value:
        import aws_sdk_securityagent.types.member_metadata

        out["metadata"] = aws_sdk_securityagent.types.member_metadata.serialize_json(
            value["metadata"]
        )
    import aws_sdk_securityagent.types._prelude.timestamp

    out["createdAt"] = aws_sdk_securityagent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_securityagent.types._prelude.timestamp

    out["updatedAt"] = aws_sdk_securityagent.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    out["createdBy"] = value["created_by"]
    out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> MembershipSummary:
    out: MembershipSummary = {}  # type: ignore[typeddict-item]
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("MembershipSummary.membership_id required")
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("MembershipSummary.application_id required")
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("MembershipSummary.agent_space_id required")
    if "memberType" in data:
        import aws_sdk_securityagent.types.membership_type

        out["member_type"] = (
            aws_sdk_securityagent.types.membership_type.deserialize_json(
                data["memberType"]
            )
        )
    else:
        raise DeserializationError("MembershipSummary.member_type required")
    if "config" in data:
        import aws_sdk_securityagent.types.membership_config

        out["config"] = aws_sdk_securityagent.types.membership_config.deserialize_json(
            data["config"]
        )
    if "metadata" in data:
        import aws_sdk_securityagent.types.member_metadata

        out["metadata"] = aws_sdk_securityagent.types.member_metadata.deserialize_json(
            data["metadata"]
        )
    if "createdAt" in data:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_securityagent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("MembershipSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_securityagent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("MembershipSummary.updated_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("MembershipSummary.created_by required")
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    else:
        raise DeserializationError("MembershipSummary.updated_by required")
    return out
