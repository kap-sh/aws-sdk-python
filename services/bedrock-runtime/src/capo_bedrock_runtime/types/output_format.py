"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#OutputFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.output_format_structure
    import capo_bedrock_runtime.types.output_format_type


class OutputFormat(TypedDict, closed=True):
    type: "capo_bedrock_runtime.types.output_format_type.OutputFormatType"
    """<p> The type of structured output format. </p>"""
    structure: (
        "capo_bedrock_runtime.types.output_format_structure.OutputFormatStructure"
    )
    """<p> The structure that the model's output must adhere to. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputFormat) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.output_format_type

    out["type"] = capo_bedrock_runtime.types.output_format_type.serialize_json(
        value["type"]
    )
    import capo_bedrock_runtime.types.output_format_structure

    out["structure"] = (
        capo_bedrock_runtime.types.output_format_structure.serialize_json(
            value["structure"]
        )
    )
    return out


def deserialize_json(data: dict) -> OutputFormat:
    out: OutputFormat = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_bedrock_runtime.types.output_format_type

        out["type"] = capo_bedrock_runtime.types.output_format_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("OutputFormat.type required")
    if "structure" in data:
        import capo_bedrock_runtime.types.output_format_structure

        out["structure"] = (
            capo_bedrock_runtime.types.output_format_structure.deserialize_json(
                data["structure"]
            )
        )
    else:
        raise DeserializationError("OutputFormat.structure required")
    return out
