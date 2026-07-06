"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpdateSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.schema_name


class UpdateSchemaRequest(TypedDict, closed=True):
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the development schema. For more information, see <a>arns</a>.</p>"""
    name: "aws_sdk_clouddirectory.types.schema_name.SchemaName"
    """<p>The name of the schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSchemaRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateSchemaRequest:
    out: UpdateSchemaRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateSchemaRequest.name required")
    return out
