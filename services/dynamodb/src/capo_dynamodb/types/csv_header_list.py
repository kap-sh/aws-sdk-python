"""Generated from Smithy shape ``com.amazonaws.dynamodb#CsvHeaderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.csv_header

CsvHeaderList: TypeAlias = list["capo_dynamodb.types.csv_header.CsvHeader"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CsvHeaderList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> CsvHeaderList:
    return [item for item in data if item is not None]
