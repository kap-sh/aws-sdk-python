"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetSchemaError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.table_alias


class BatchGetSchemaError(TypedDict):
    name: "aws_sdk_cleanrooms.types.table_alias.TableAlias"
    """<p>An error name for the error.</p>"""
    code: "str"
    """<p>An error code for the error. </p>"""
    message: "str"
    """<p>An error message for the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSchemaError) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetSchemaError:
    out: BatchGetSchemaError = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("BatchGetSchemaError.name required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("BatchGetSchemaError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchGetSchemaError.message required")
    return out
