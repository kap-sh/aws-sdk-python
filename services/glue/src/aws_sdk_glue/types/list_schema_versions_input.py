"""Generated from Smithy shape ``com.amazonaws.glue#ListSchemaVersionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.max_results_number
    import aws_sdk_glue.types.schema_id
    import aws_sdk_glue.types.schema_registry_token_string


class ListSchemaVersionsInput(TypedDict):
    schema_id: "aws_sdk_glue.types.schema_id.SchemaId"
    """<p>This is a wrapper structure to contain schema identity fields. The structure contains:</p> <ul> <li> <p>SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> <li> <p>SchemaId$SchemaName: The name of the schema. Either <code>SchemaArn</code> or <code>SchemaName</code> and <code>RegistryName</code> has to be provided.</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_glue.types.max_results_number.MaxResultsNumber"]
    """<p>Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page.</p>"""
    next_token: NotRequired[
        "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
    ]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSchemaVersionsInput) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.schema_id

    out["SchemaId"] = aws_sdk_glue.types.schema_id.serialize_aws_json_1_1(
        value["schema_id"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSchemaVersionsInput:
    out: ListSchemaVersionsInput = {}  # type: ignore[typeddict-item]
    if "SchemaId" in data:
        import aws_sdk_glue.types.schema_id

        out["schema_id"] = aws_sdk_glue.types.schema_id.deserialize_aws_json_1_1(
            data["SchemaId"]
        )
    else:
        raise DeserializationError("ListSchemaVersionsInput.schema_id required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
