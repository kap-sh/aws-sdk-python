"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InputFile``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.file_source
    import aws_sdk_bedrock_agent_runtime.types.file_use_case


class InputFile(TypedDict):
    name: "str"
    """<p>The name of the source file.</p>"""
    source: "aws_sdk_bedrock_agent_runtime.types.file_source.FileSource"
    """<p>Specifies where the files are located.</p>"""
    use_case: "aws_sdk_bedrock_agent_runtime.types.file_use_case.FileUseCase"
    """<p>Specifies how the source files will be used by the code interpreter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputFile) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_bedrock_agent_runtime.types.file_source

    out["source"] = aws_sdk_bedrock_agent_runtime.types.file_source.serialize_json(
        value["source"]
    )
    import aws_sdk_bedrock_agent_runtime.types.file_use_case

    out["useCase"] = aws_sdk_bedrock_agent_runtime.types.file_use_case.serialize_json(
        value["use_case"]
    )
    return out


def deserialize_json(data: dict) -> InputFile:
    out: InputFile = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("InputFile.name required")
    if "source" in data:
        import aws_sdk_bedrock_agent_runtime.types.file_source

        out["source"] = (
            aws_sdk_bedrock_agent_runtime.types.file_source.deserialize_json(
                data["source"]
            )
        )
    else:
        raise DeserializationError("InputFile.source required")
    if "useCase" in data:
        import aws_sdk_bedrock_agent_runtime.types.file_use_case

        out["use_case"] = (
            aws_sdk_bedrock_agent_runtime.types.file_use_case.deserialize_json(
                data["useCase"]
            )
        )
    else:
        raise DeserializationError("InputFile.use_case required")
    return out
