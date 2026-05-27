"""Generated from Smithy shape ``com.amazonaws.dynamodb#CsvOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.csv_delimiter
    import aws_sdk_dynamodb.types.csv_header_list


class CsvOptions(TypedDict):
    delimiter: NotRequired["aws_sdk_dynamodb.types.csv_delimiter.CsvDelimiter"]
    """<p> The delimiter used for separating items in the CSV file being imported. </p>"""
    header_list: NotRequired["aws_sdk_dynamodb.types.csv_header_list.CsvHeaderList"]
    """<p> List of the headers used to specify a common header for all source CSV files being imported. If this field is specified then the first line of each CSV file is treated as data instead of the header. If this field is not specified the the first line of each CSV file is treated as the header. </p>"""
