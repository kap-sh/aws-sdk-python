"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportTableOutput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.import_table_description


class ImportTableOutput(TypedDict):
    import_table_description: (
        "aws_sdk_dynamodb.types.import_table_description.ImportTableDescription"
    )
    """<p> Represents the properties of the table created for the import, and parameters of the import. The import parameters include import status, how many items were processed, and how many errors were encountered. </p>"""
