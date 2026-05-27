"""Generated from Smithy shape ``com.amazonaws.dynamodb#CsvHeaderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.csv_header

CsvHeaderList: TypeAlias = list["aws_sdk_dynamodb.types.csv_header.CsvHeader"]
