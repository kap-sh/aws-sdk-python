"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateAgentSpaceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_securityagent.types.agent_name
    import aws_sdk_securityagent.types.agent_space_id
    import aws_sdk_securityagent.types.aws_resources
    import aws_sdk_securityagent.types.code_review_settings
    import aws_sdk_securityagent.types.kms_key_id
    import aws_sdk_securityagent.types.target_domain_id_list


class CreateAgentSpaceOutput(TypedDict):
    agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the created agent space.</p>"""
    name: "aws_sdk_securityagent.types.agent_name.AgentName"
    """<p>The name of the agent space.</p>"""
    description: NotRequired["str"]
    """<p>The description of the agent space.</p>"""
    aws_resources: NotRequired["aws_sdk_securityagent.types.aws_resources.AWSResources"]
    """<p>The AWS resources associated with the agent space.</p>"""
    target_domain_ids: NotRequired[
        "aws_sdk_securityagent.types.target_domain_id_list.TargetDomainIdList"
    ]
    """<p>The list of target domain identifiers associated with the agent space.</p>"""
    code_review_settings: NotRequired[
        "aws_sdk_securityagent.types.code_review_settings.CodeReviewSettings"
    ]
    """<p>The code review settings for the agent space.</p>"""
    kms_key_id: NotRequired["aws_sdk_securityagent.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the AWS KMS key used to encrypt data in the agent space.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the agent space was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the agent space was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentSpaceOutput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
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
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "created_at" in value:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_securityagent.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_securityagent.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAgentSpaceOutput:
    out: CreateAgentSpaceOutput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("CreateAgentSpaceOutput.agent_space_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAgentSpaceOutput.name required")
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
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "createdAt" in data:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_securityagent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_securityagent.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_securityagent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
