"""Generated from Smithy shape ``com.amazonaws.codepipeline#EnvironmentVariable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.environment_variable_name
    import aws_sdk_codepipeline.types.environment_variable_type
    import aws_sdk_codepipeline.types.environment_variable_value


class EnvironmentVariable(TypedDict, closed=True):
    name: "aws_sdk_codepipeline.types.environment_variable_name.EnvironmentVariableName"
    """<p>The environment variable name in the key-value pair.</p>"""
    value: (
        "aws_sdk_codepipeline.types.environment_variable_value.EnvironmentVariableValue"
    )
    """<p>The environment variable value in the key-value pair.</p>"""
    type: NotRequired[
        "aws_sdk_codepipeline.types.environment_variable_type.EnvironmentVariableType"
    ]
    """<p>Specifies the type of use for the environment variable value. The value can be either <code>PLAINTEXT</code> or <code>SECRETS_MANAGER</code>. If the value is <code>SECRETS_MANAGER</code>, provide the Secrets reference in the EnvironmentVariable value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentVariable) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    if "type" in value:
        import aws_sdk_codepipeline.types.environment_variable_type

        out["type"] = (
            aws_sdk_codepipeline.types.environment_variable_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentVariable:
    out: EnvironmentVariable = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("EnvironmentVariable.name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("EnvironmentVariable.value required")
    if "type" in data:
        import aws_sdk_codepipeline.types.environment_variable_type

        out["type"] = (
            aws_sdk_codepipeline.types.environment_variable_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    return out
