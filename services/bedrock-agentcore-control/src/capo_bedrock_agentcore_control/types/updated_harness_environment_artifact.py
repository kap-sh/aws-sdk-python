"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedHarnessEnvironmentArtifact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_environment_artifact


class UpdatedHarnessEnvironmentArtifact(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_environment_artifact.HarnessEnvironmentArtifact"
    ]
    """<p>The updated environment artifact value, or null to clear the existing configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedHarnessEnvironmentArtifact) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_bedrock_agentcore_control.types.harness_environment_artifact

        out["optionalValue"] = (
            capo_bedrock_agentcore_control.types.harness_environment_artifact.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedHarnessEnvironmentArtifact:
    out: UpdatedHarnessEnvironmentArtifact = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import capo_bedrock_agentcore_control.types.harness_environment_artifact

        out["optional_value"] = (
            capo_bedrock_agentcore_control.types.harness_environment_artifact.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
