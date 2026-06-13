"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetSchemaOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.batch_get_schema_error_list
    import aws_sdk_cleanrooms.types.schema_list


class BatchGetSchemaOutput(TypedDict):
    schemas: "aws_sdk_cleanrooms.types.schema_list.SchemaList"
    """<p>The retrieved list of schemas.</p>"""
    errors: (
        "aws_sdk_cleanrooms.types.batch_get_schema_error_list.BatchGetSchemaErrorList"
    )
    """<p>Error reasons for schemas that could not be retrieved. One error is returned for every schema that could not be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSchemaOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.schema_list

    out["schemas"] = aws_sdk_cleanrooms.types.schema_list.serialize_json(
        value["schemas"]
    )
    import aws_sdk_cleanrooms.types.batch_get_schema_error_list

    out["errors"] = aws_sdk_cleanrooms.types.batch_get_schema_error_list.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetSchemaOutput:
    out: BatchGetSchemaOutput = {}  # type: ignore[typeddict-item]
    if "schemas" in data:
        import aws_sdk_cleanrooms.types.schema_list

        out["schemas"] = aws_sdk_cleanrooms.types.schema_list.deserialize_json(
            data["schemas"]
        )
    else:
        raise DeserializationError("BatchGetSchemaOutput.schemas required")
    if "errors" in data:
        import aws_sdk_cleanrooms.types.batch_get_schema_error_list

        out["errors"] = (
            aws_sdk_cleanrooms.types.batch_get_schema_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchGetSchemaOutput.errors required")
    return out
