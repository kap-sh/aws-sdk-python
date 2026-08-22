"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSkill``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_skill_git_source
    import capo_bedrock_agentcore_control.types.harness_skill_path
    import capo_bedrock_agentcore_control.types.harness_skill_s3_source


class _HarnessSkill_path(TypedDict, closed=True):
    path: "capo_bedrock_agentcore_control.types.harness_skill_path.HarnessSkillPath"


class _HarnessSkill_s3(TypedDict, closed=True):
    s3: "capo_bedrock_agentcore_control.types.harness_skill_s3_source.HarnessSkillS3Source"


class _HarnessSkill_git(TypedDict, closed=True):
    git: "capo_bedrock_agentcore_control.types.harness_skill_git_source.HarnessSkillGitSource"


HarnessSkill: TypeAlias = _HarnessSkill_path | _HarnessSkill_s3 | _HarnessSkill_git


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSkill) -> dict:
    if "path" in value:
        return {"path": value["path"]}
    elif "s3" in value:
        import capo_bedrock_agentcore_control.types.harness_skill_s3_source

        return {
            "s3": capo_bedrock_agentcore_control.types.harness_skill_s3_source.serialize_json(
                value["s3"]
            )
        }
    elif "git" in value:
        import capo_bedrock_agentcore_control.types.harness_skill_git_source

        return {
            "git": capo_bedrock_agentcore_control.types.harness_skill_git_source.serialize_json(
                value["git"]
            )
        }
    else:
        raise SerializationError("HarnessSkill: no variant present")


def deserialize_json(data: dict) -> HarnessSkill:
    if data.get("path") is not None:
        return {"path": data["path"]}
    elif data.get("s3") is not None:
        import capo_bedrock_agentcore_control.types.harness_skill_s3_source

        return {
            "s3": capo_bedrock_agentcore_control.types.harness_skill_s3_source.deserialize_json(
                data["s3"]
            )
        }
    elif data.get("git") is not None:
        import capo_bedrock_agentcore_control.types.harness_skill_git_source

        return {
            "git": capo_bedrock_agentcore_control.types.harness_skill_git_source.deserialize_json(
                data["git"]
            )
        }
    else:
        raise DeserializationError("HarnessSkill: no recognized variant key")
