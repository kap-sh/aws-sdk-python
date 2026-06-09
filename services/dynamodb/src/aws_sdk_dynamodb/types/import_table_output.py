"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportTableOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.import_table_description


class ImportTableOutput(TypedDict):
    import_table_description: (
        "aws_sdk_dynamodb.types.import_table_description.ImportTableDescription"
    )
    """<p> Represents the properties of the table created for the import, and parameters of the import. The import parameters include import status, how many items were processed, and how many errors were encountered. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportTableOutput) -> dict:
    out: dict = {}
    import aws_sdk_dynamodb.types.import_table_description

    out["ImportTableDescription"] = (
        aws_sdk_dynamodb.types.import_table_description.serialize_aws_json_1_0(
            value["import_table_description"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportTableOutput:
    out: ImportTableOutput = {}  # type: ignore[typeddict-item]
    if "ImportTableDescription" in data:
        import aws_sdk_dynamodb.types.import_table_description

        out["import_table_description"] = (
            aws_sdk_dynamodb.types.import_table_description.deserialize_aws_json_1_0(
                data["ImportTableDescription"]
            )
        )
    else:
        raise DeserializationError(
            "ImportTableOutput.import_table_description required"
        )
    return out
