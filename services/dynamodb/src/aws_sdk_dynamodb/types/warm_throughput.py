"""Generated from Smithy shape ``com.amazonaws.dynamodb#WarmThroughput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.long_object


class WarmThroughput(TypedDict):
    read_units_per_second: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p>Represents the number of read operations your base table can instantaneously support.</p>"""
    write_units_per_second: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p>Represents the number of write operations your base table can instantaneously support.</p>"""
