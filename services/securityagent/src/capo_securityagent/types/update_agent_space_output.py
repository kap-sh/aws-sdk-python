"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateAgentSpaceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.agent_name
    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.aws_resources
    import capo_securityagent.types.code_review_settings
    import capo_securityagent.types.target_domain_id_list


class UpdateAgentSpaceOutput(TypedDict, closed=True):
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the updated agent space.</p>"""
    name: "capo_securityagent.types.agent_name.AgentName"
    """<p>The name of the agent space.</p>"""
    description: NotRequired["str"]
    """<p>The description of the agent space.</p>"""
    aws_resources: NotRequired["capo_securityagent.types.aws_resources.AWSResources"]
    """<p>The AWS resources associated with the agent space.</p>"""
    target_domain_ids: NotRequired[
        "capo_securityagent.types.target_domain_id_list.TargetDomainIdList"
    ]
    """<p>The list of target domain identifiers associated with the agent space.</p>"""
    code_review_settings: NotRequired[
        "capo_securityagent.types.code_review_settings.CodeReviewSettings"
    ]
    """<p>The code review settings for the agent space.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the agent space was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the agent space was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentSpaceOutput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "aws_resources" in value:
        import capo_securityagent.types.aws_resources

        out["awsResources"] = capo_securityagent.types.aws_resources.serialize_json(
            value["aws_resources"]
        )
    if "target_domain_ids" in value:
        import capo_securityagent.types.target_domain_id_list

        out["targetDomainIds"] = (
            capo_securityagent.types.target_domain_id_list.serialize_json(
                value["target_domain_ids"]
            )
        )
    if "code_review_settings" in value:
        import capo_securityagent.types.code_review_settings

        out["codeReviewSettings"] = (
            capo_securityagent.types.code_review_settings.serialize_json(
                value["code_review_settings"]
            )
        )
    if "created_at" in value:
        import capo_securityagent.types._prelude.timestamp

        out["createdAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent.types._prelude.timestamp

        out["updatedAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentSpaceOutput:
    out: UpdateAgentSpaceOutput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("UpdateAgentSpaceOutput.agent_space_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateAgentSpaceOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "awsResources" in data:
        import capo_securityagent.types.aws_resources

        out["aws_resources"] = capo_securityagent.types.aws_resources.deserialize_json(
            data["awsResources"]
        )
    if "targetDomainIds" in data:
        import capo_securityagent.types.target_domain_id_list

        out["target_domain_ids"] = (
            capo_securityagent.types.target_domain_id_list.deserialize_json(
                data["targetDomainIds"]
            )
        )
    if "codeReviewSettings" in data:
        import capo_securityagent.types.code_review_settings

        out["code_review_settings"] = (
            capo_securityagent.types.code_review_settings.deserialize_json(
                data["codeReviewSettings"]
            )
        )
    if "createdAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["created_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["updated_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
