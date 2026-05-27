"""Generated from Smithy shape ``com.amazonaws.dynamodb#InputFormatOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.csv_options


class InputFormatOptions(TypedDict):
    csv: NotRequired["aws_sdk_dynamodb.types.csv_options.CsvOptions"]
    """<p> The options for imported source files in CSV format. The values are Delimiter and HeaderList. </p>"""
