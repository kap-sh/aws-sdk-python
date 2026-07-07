"""Generated from Smithy shape ``com.amazonaws.greengrass#FunctionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__boolean
    import aws_sdk_greengrass.types.__integer
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.encoding_type
    import aws_sdk_greengrass.types.function_configuration_environment


class FunctionConfiguration(TypedDict, closed=True):
    encoding_type: NotRequired["aws_sdk_greengrass.types.encoding_type.EncodingType"]
    """The expected encoding type of the input payload for the function. The default is ''json''."""
    environment: NotRequired[
        "aws_sdk_greengrass.types.function_configuration_environment.FunctionConfigurationEnvironment"
    ]
    """The environment configuration of the function."""
    exec_args: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The execution arguments."""
    executable: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The name of the function executable."""
    memory_size: NotRequired["aws_sdk_greengrass.types.__integer.__integer"]
    """The memory size, in KB, which the function requires. This setting is not applicable and should be cleared when you run the Lambda function without containerization."""
    pinned: NotRequired["aws_sdk_greengrass.types.__boolean.__boolean"]
    """True if the function is pinned. Pinned means the function is long-lived and starts when the core starts."""
    timeout: NotRequired["aws_sdk_greengrass.types.__integer.__integer"]
    """The allowed function execution time, after which Lambda should terminate the function. This timeout still applies to pinned Lambda functions for each request."""
    function_runtime_override: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The Lambda runtime supported by Greengrass which is to be used instead of the one specified in the Lambda function."""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionConfiguration) -> dict:
    out: dict = {}
    if "encoding_type" in value:
        import aws_sdk_greengrass.types.encoding_type

        out["EncodingType"] = aws_sdk_greengrass.types.encoding_type.serialize_json(
            value["encoding_type"]
        )
    if "environment" in value:
        import aws_sdk_greengrass.types.function_configuration_environment

        out["Environment"] = (
            aws_sdk_greengrass.types.function_configuration_environment.serialize_json(
                value["environment"]
            )
        )
    if "exec_args" in value:
        out["ExecArgs"] = value["exec_args"]
    if "executable" in value:
        out["Executable"] = value["executable"]
    if "memory_size" in value:
        out["MemorySize"] = value["memory_size"]
    if "pinned" in value:
        out["Pinned"] = value["pinned"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "function_runtime_override" in value:
        out["FunctionRuntimeOverride"] = value["function_runtime_override"]
    return out


def deserialize_json(data: dict) -> FunctionConfiguration:
    out: FunctionConfiguration = {}  # type: ignore[typeddict-item]
    if "EncodingType" in data:
        import aws_sdk_greengrass.types.encoding_type

        out["encoding_type"] = aws_sdk_greengrass.types.encoding_type.deserialize_json(
            data["EncodingType"]
        )
    if "Environment" in data:
        import aws_sdk_greengrass.types.function_configuration_environment

        out["environment"] = (
            aws_sdk_greengrass.types.function_configuration_environment.deserialize_json(
                data["Environment"]
            )
        )
    if "ExecArgs" in data:
        out["exec_args"] = data["ExecArgs"]
    if "Executable" in data:
        out["executable"] = data["Executable"]
    if "MemorySize" in data:
        out["memory_size"] = data["MemorySize"]
    if "Pinned" in data:
        out["pinned"] = data["Pinned"]
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    if "FunctionRuntimeOverride" in data:
        out["function_runtime_override"] = data["FunctionRuntimeOverride"]
    return out
