"""Generated from Smithy shape ``com.amazonaws.glue#DeleteSchemaVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.schema_version_error_list


class DeleteSchemaVersionsResponse(TypedDict, closed=True):
    schema_version_errors: NotRequired[
        "aws_sdk_glue.types.schema_version_error_list.SchemaVersionErrorList"
    ]
    """<p>A list of <code>SchemaVersionErrorItem</code> objects, each containing an error and schema version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSchemaVersionsResponse) -> dict:
    out: dict = {}
    if "schema_version_errors" in value:
        import aws_sdk_glue.types.schema_version_error_list

        out["SchemaVersionErrors"] = (
            aws_sdk_glue.types.schema_version_error_list.serialize_aws_json_1_1(
                value["schema_version_errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSchemaVersionsResponse:
    out: DeleteSchemaVersionsResponse = {}  # type: ignore[typeddict-item]
    if "SchemaVersionErrors" in data:
        import aws_sdk_glue.types.schema_version_error_list

        out["schema_version_errors"] = (
            aws_sdk_glue.types.schema_version_error_list.deserialize_aws_json_1_1(
                data["SchemaVersionErrors"]
            )
        )
    return out
