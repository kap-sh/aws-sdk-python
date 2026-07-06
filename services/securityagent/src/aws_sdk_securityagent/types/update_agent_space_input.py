"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateAgentSpaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.agent_name
    import aws_sdk_securityagent.types.agent_space_id
    import aws_sdk_securityagent.types.aws_resources
    import aws_sdk_securityagent.types.code_review_settings
    import aws_sdk_securityagent.types.target_domain_id_list


class UpdateAgentSpaceInput(TypedDict, closed=True):
    agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space to update.</p>"""
    name: NotRequired["aws_sdk_securityagent.types.agent_name.AgentName"]
    """<p>The updated name of the agent space.</p>"""
    description: NotRequired["str"]
    """<p>The updated description of the agent space.</p>"""
    aws_resources: NotRequired["aws_sdk_securityagent.types.aws_resources.AWSResources"]
    """<p>The updated AWS resources to associate with the agent space.</p>"""
    target_domain_ids: NotRequired[
        "aws_sdk_securityagent.types.target_domain_id_list.TargetDomainIdList"
    ]
    """<p>The updated list of target domain identifiers to associate with the agent space.</p>"""
    code_review_settings: NotRequired[
        "aws_sdk_securityagent.types.code_review_settings.CodeReviewSettings"
    ]
    """<p>The updated code review settings for the agent space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentSpaceInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "aws_resources" in value:
        import aws_sdk_securityagent.types.aws_resources

        out["awsResources"] = aws_sdk_securityagent.types.aws_resources.serialize_json(
            value["aws_resources"]
        )
    if "target_domain_ids" in value:
        import aws_sdk_securityagent.types.target_domain_id_list

        out["targetDomainIds"] = (
            aws_sdk_securityagent.types.target_domain_id_list.serialize_json(
                value["target_domain_ids"]
            )
        )
    if "code_review_settings" in value:
        import aws_sdk_securityagent.types.code_review_settings

        out["codeReviewSettings"] = (
            aws_sdk_securityagent.types.code_review_settings.serialize_json(
                value["code_review_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentSpaceInput:
    out: UpdateAgentSpaceInput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("UpdateAgentSpaceInput.agent_space_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "awsResources" in data:
        import aws_sdk_securityagent.types.aws_resources

        out["aws_resources"] = (
            aws_sdk_securityagent.types.aws_resources.deserialize_json(
                data["awsResources"]
            )
        )
    if "targetDomainIds" in data:
        import aws_sdk_securityagent.types.target_domain_id_list

        out["target_domain_ids"] = (
            aws_sdk_securityagent.types.target_domain_id_list.deserialize_json(
                data["targetDomainIds"]
            )
        )
    if "codeReviewSettings" in data:
        import aws_sdk_securityagent.types.code_review_settings

        out["code_review_settings"] = (
            aws_sdk_securityagent.types.code_review_settings.deserialize_json(
                data["codeReviewSettings"]
            )
        )
    return out
