"""Generated from Smithy shape ``com.amazonaws.glue#CodeGenNodeArg``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.boolean
    import aws_sdk_glue.types.code_gen_arg_name
    import aws_sdk_glue.types.code_gen_arg_value


class CodeGenNodeArg(TypedDict, closed=True):
    name: "aws_sdk_glue.types.code_gen_arg_name.CodeGenArgName"
    """<p>The name of the argument or property.</p>"""
    value: "aws_sdk_glue.types.code_gen_arg_value.CodeGenArgValue"
    """<p>The value of the argument or property.</p>"""
    param: "aws_sdk_glue.types.boolean.Boolean"
    """<p>True if the value is used as a parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeGenNodeArg) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    out["Param"] = value.get("param", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeGenNodeArg:
    out: CodeGenNodeArg = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CodeGenNodeArg.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("CodeGenNodeArg.value required")
    if "Param" in data:
        out["param"] = data["Param"]
    else:
        out["param"] = False
    return out
