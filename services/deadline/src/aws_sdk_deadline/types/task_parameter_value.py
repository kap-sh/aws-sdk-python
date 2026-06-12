"""Generated from Smithy shape ``com.amazonaws.deadline#TaskParameterValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.float_string
    import aws_sdk_deadline.types.int_string
    import aws_sdk_deadline.types.parameter_string
    import aws_sdk_deadline.types.path_string
    import aws_sdk_deadline.types.string


class _TaskParameterValue_int(TypedDict):
    int: "aws_sdk_deadline.types.int_string.IntString"


class _TaskParameterValue_float(TypedDict):
    float: "aws_sdk_deadline.types.float_string.FloatString"


class _TaskParameterValue_string(TypedDict):
    string: "aws_sdk_deadline.types.parameter_string.ParameterString"


class _TaskParameterValue_path(TypedDict):
    path: "aws_sdk_deadline.types.path_string.PathString"


class _TaskParameterValue_chunkInt(TypedDict):
    chunkInt: "aws_sdk_deadline.types.string.String"


TaskParameterValue: TypeAlias = (
    _TaskParameterValue_int
    | _TaskParameterValue_float
    | _TaskParameterValue_string
    | _TaskParameterValue_path
    | _TaskParameterValue_chunkInt
)


# --- restJson1 ser/de ---
def serialize_json(value: TaskParameterValue) -> dict:
    if "int" in value:
        return {"int": value["int"]}
    elif "float" in value:
        return {"float": value["float"]}
    elif "string" in value:
        return {"string": value["string"]}
    elif "path" in value:
        return {"path": value["path"]}
    elif "chunkInt" in value:
        return {"chunkInt": value["chunkInt"]}
    else:
        raise SerializationError("TaskParameterValue: no variant present")


def deserialize_json(data: dict) -> TaskParameterValue:
    if "int" in data:
        return {"int": data["int"]}
    elif "float" in data:
        return {"float": data["float"]}
    elif "string" in data:
        return {"string": data["string"]}
    elif "path" in data:
        return {"path": data["path"]}
    elif "chunkInt" in data:
        return {"chunkInt": data["chunkInt"]}
    else:
        raise DeserializationError("TaskParameterValue: no recognized variant key")
