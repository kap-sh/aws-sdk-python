"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedSynchronizationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.synchronization_configuration


class UpdatedSynchronizationConfiguration(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_bedrock_agentcore_control.types.synchronization_configuration.SynchronizationConfiguration"
    ]
    """<p>The updated synchronization configuration value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedSynchronizationConfiguration) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_bedrock_agentcore_control.types.synchronization_configuration

        out["optionalValue"] = (
            capo_bedrock_agentcore_control.types.synchronization_configuration.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedSynchronizationConfiguration:
    out: UpdatedSynchronizationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("optionalValue") is not None:
        import capo_bedrock_agentcore_control.types.synchronization_configuration

        out["optional_value"] = (
            capo_bedrock_agentcore_control.types.synchronization_configuration.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
