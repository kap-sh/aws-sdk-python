"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessSkill``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_skill_git_source
    import aws_sdk_bedrock_agentcore.types.harness_skill_path
    import aws_sdk_bedrock_agentcore.types.harness_skill_s3_source


class _HarnessSkill_path(TypedDict):
    path: "aws_sdk_bedrock_agentcore.types.harness_skill_path.HarnessSkillPath"


class _HarnessSkill_s3(TypedDict):
    s3: "aws_sdk_bedrock_agentcore.types.harness_skill_s3_source.HarnessSkillS3Source"


class _HarnessSkill_git(TypedDict):
    git: (
        "aws_sdk_bedrock_agentcore.types.harness_skill_git_source.HarnessSkillGitSource"
    )


HarnessSkill: TypeAlias = _HarnessSkill_path | _HarnessSkill_s3 | _HarnessSkill_git


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSkill) -> dict:
    if "path" in value:
        return {"path": value["path"]}
    elif "s3" in value:
        import aws_sdk_bedrock_agentcore.types.harness_skill_s3_source

        return {
            "s3": aws_sdk_bedrock_agentcore.types.harness_skill_s3_source.serialize_json(
                value["s3"]
            )
        }
    elif "git" in value:
        import aws_sdk_bedrock_agentcore.types.harness_skill_git_source

        return {
            "git": aws_sdk_bedrock_agentcore.types.harness_skill_git_source.serialize_json(
                value["git"]
            )
        }
    else:
        raise SerializationError("HarnessSkill: no variant present")


def deserialize_json(data: dict) -> HarnessSkill:
    if "path" in data:
        return {"path": data["path"]}
    elif "s3" in data:
        import aws_sdk_bedrock_agentcore.types.harness_skill_s3_source

        return {
            "s3": aws_sdk_bedrock_agentcore.types.harness_skill_s3_source.deserialize_json(
                data["s3"]
            )
        }
    elif "git" in data:
        import aws_sdk_bedrock_agentcore.types.harness_skill_git_source

        return {
            "git": aws_sdk_bedrock_agentcore.types.harness_skill_git_source.deserialize_json(
                data["git"]
            )
        }
    else:
        raise DeserializationError("HarnessSkill: no recognized variant key")
