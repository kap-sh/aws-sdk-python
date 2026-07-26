"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedDescriptors``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.updated_descriptors_union


class UpdatedDescriptors(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_bedrock_agentcore_control.types.updated_descriptors_union.UpdatedDescriptorsUnion"
    ]
    """<p>The updated descriptors value. Contains per-descriptor-type wrappers that are each independently updatable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedDescriptors) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_bedrock_agentcore_control.types.updated_descriptors_union

        out["optionalValue"] = (
            capo_bedrock_agentcore_control.types.updated_descriptors_union.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedDescriptors:
    out: UpdatedDescriptors = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import capo_bedrock_agentcore_control.types.updated_descriptors_union

        out["optional_value"] = (
            capo_bedrock_agentcore_control.types.updated_descriptors_union.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
