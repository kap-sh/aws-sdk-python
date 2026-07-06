"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetSchemaOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.schema


class GetSchemaOutput(TypedDict, closed=True):
    schema: "aws_sdk_cleanrooms.types.schema.Schema"
    """<p>The entire schema object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.schema

    out["schema"] = aws_sdk_cleanrooms.types.schema.serialize_json(value["schema"])
    return out


def deserialize_json(data: dict) -> GetSchemaOutput:
    out: GetSchemaOutput = {}  # type: ignore[typeddict-item]
    if "schema" in data:
        import aws_sdk_cleanrooms.types.schema

        out["schema"] = aws_sdk_cleanrooms.types.schema.deserialize_json(data["schema"])
    else:
        raise DeserializationError("GetSchemaOutput.schema required")
    return out
