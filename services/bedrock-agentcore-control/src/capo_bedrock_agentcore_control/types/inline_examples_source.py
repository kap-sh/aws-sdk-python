"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InlineExamplesSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.dataset_example_list


class InlineExamplesSource(TypedDict, closed=True):
    examples: (
        "capo_bedrock_agentcore_control.types.dataset_example_list.DatasetExampleList"
    )
    """<p> Examples to add. Each example is assigned an auto-generated UUID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineExamplesSource) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.dataset_example_list

    out["examples"] = (
        capo_bedrock_agentcore_control.types.dataset_example_list.serialize_json(
            value["examples"]
        )
    )
    return out


def deserialize_json(data: dict) -> InlineExamplesSource:
    out: InlineExamplesSource = {}  # type: ignore[typeddict-item]
    if "examples" in data:
        import capo_bedrock_agentcore_control.types.dataset_example_list

        out["examples"] = (
            capo_bedrock_agentcore_control.types.dataset_example_list.deserialize_json(
                data["examples"]
            )
        )
    else:
        raise DeserializationError("InlineExamplesSource.examples required")
    return out
