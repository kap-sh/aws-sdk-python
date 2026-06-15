"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessSkillS3Source``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_skill_s3_uri


class HarnessSkillS3Source(TypedDict):
    uri: "aws_sdk_bedrock_agentcore.types.harness_skill_s3_uri.HarnessSkillS3Uri"
    """<p>The S3 URI pointing to the skill directory (e.g., s3://bucket/skills/my-skill/).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSkillS3Source) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> HarnessSkillS3Source:
    out: HarnessSkillS3Source = {}  # type: ignore[typeddict-item]
    if "uri" in data:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("HarnessSkillS3Source.uri required")
    return out
