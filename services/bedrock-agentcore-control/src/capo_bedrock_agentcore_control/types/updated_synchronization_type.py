"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedSynchronizationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.synchronization_type


class UpdatedSynchronizationType(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_bedrock_agentcore_control.types.synchronization_type.SynchronizationType"
    ]
    """<p>The updated synchronization type value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedSynchronizationType) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_bedrock_agentcore_control.types.synchronization_type

        out["optionalValue"] = (
            capo_bedrock_agentcore_control.types.synchronization_type.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedSynchronizationType:
    out: UpdatedSynchronizationType = {}  # type: ignore[typeddict-item]
    if data.get("optionalValue") is not None:
        import capo_bedrock_agentcore_control.types.synchronization_type

        out["optional_value"] = (
            capo_bedrock_agentcore_control.types.synchronization_type.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
