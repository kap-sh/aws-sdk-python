"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateVariableRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.string


class UpdateVariableRequest(TypedDict):
    name: "aws_sdk_frauddetector.types.string.string"
    """<p>The name of the variable.</p>"""
    default_value: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The new default value of the variable.</p>"""
    description: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The new description.</p>"""
    variable_type: NotRequired["aws_sdk_frauddetector.types.string.string"]
    r"""<p>The variable type. For more information see <a href=\"https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types\">Variable types</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateVariableRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "description" in value:
        out["description"] = value["description"]
    if "variable_type" in value:
        out["variableType"] = value["variable_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateVariableRequest:
    out: UpdateVariableRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateVariableRequest.name required")
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    if "description" in data:
        out["description"] = data["description"]
    if "variableType" in data:
        out["variable_type"] = data["variableType"]
    return out
