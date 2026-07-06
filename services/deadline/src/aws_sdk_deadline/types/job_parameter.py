"""Generated from Smithy shape ``com.amazonaws.deadline#JobParameter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.float_string
    import aws_sdk_deadline.types.int_string
    import aws_sdk_deadline.types.parameter_string
    import aws_sdk_deadline.types.path_string


class _JobParameter_int(TypedDict, closed=True):
    int: "aws_sdk_deadline.types.int_string.IntString"


class _JobParameter_float(TypedDict, closed=True):
    float: "aws_sdk_deadline.types.float_string.FloatString"


class _JobParameter_string(TypedDict, closed=True):
    string: "aws_sdk_deadline.types.parameter_string.ParameterString"


class _JobParameter_path(TypedDict, closed=True):
    path: "aws_sdk_deadline.types.path_string.PathString"


JobParameter: TypeAlias = (
    _JobParameter_int | _JobParameter_float | _JobParameter_string | _JobParameter_path
)


# --- restJson1 ser/de ---
def serialize_json(value: JobParameter) -> dict:
    if "int" in value:
        return {"int": value["int"]}
    elif "float" in value:
        return {"float": value["float"]}
    elif "string" in value:
        return {"string": value["string"]}
    elif "path" in value:
        return {"path": value["path"]}
    else:
        raise SerializationError("JobParameter: no variant present")


def deserialize_json(data: dict) -> JobParameter:
    if "int" in data:
        return {"int": data["int"]}
    elif "float" in data:
        return {"float": data["float"]}
    elif "string" in data:
        return {"string": data["string"]}
    elif "path" in data:
        return {"path": data["path"]}
    else:
        raise DeserializationError("JobParameter: no recognized variant key")
