"""Generated from Smithy shape ``com.amazonaws.devicefarm#EnvironmentVariable``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.environment_variable_name
    import aws_sdk_device_farm.types.environment_variable_value


class EnvironmentVariable(TypedDict, closed=True):
    name: "aws_sdk_device_farm.types.environment_variable_name.EnvironmentVariableName"
    """<p>The name of the environment variable.</p>"""
    value: (
        "aws_sdk_device_farm.types.environment_variable_value.EnvironmentVariableValue"
    )
    """<p>The value of the environment variable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentVariable) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
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
    return out
