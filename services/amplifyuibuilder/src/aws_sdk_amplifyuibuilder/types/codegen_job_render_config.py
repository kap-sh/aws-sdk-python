"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJobRenderConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.react_start_codegen_job_data


class _CodegenJobRenderConfig_react(TypedDict, closed=True):
    react: "aws_sdk_amplifyuibuilder.types.react_start_codegen_job_data.ReactStartCodegenJobData"


CodegenJobRenderConfig: TypeAlias = _CodegenJobRenderConfig_react


# --- restJson1 ser/de ---
def serialize_json(value: CodegenJobRenderConfig) -> dict:
    if "react" in value:
        import aws_sdk_amplifyuibuilder.types.react_start_codegen_job_data

        return {
            "react": aws_sdk_amplifyuibuilder.types.react_start_codegen_job_data.serialize_json(
                value["react"]
            )
        }
    else:
        raise SerializationError("CodegenJobRenderConfig: no variant present")


def deserialize_json(data: dict) -> CodegenJobRenderConfig:
    if "react" in data:
        import aws_sdk_amplifyuibuilder.types.react_start_codegen_job_data

        return {
            "react": aws_sdk_amplifyuibuilder.types.react_start_codegen_job_data.deserialize_json(
                data["react"]
            )
        }
    else:
        raise DeserializationError("CodegenJobRenderConfig: no recognized variant key")
