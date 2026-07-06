"""Generated from Smithy shape ``com.amazonaws.dynamodb#CsvOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.csv_delimiter
    import aws_sdk_dynamodb.types.csv_header_list


class CsvOptions(TypedDict, closed=True):
    delimiter: NotRequired["aws_sdk_dynamodb.types.csv_delimiter.CsvDelimiter"]
    """<p> The delimiter used for separating items in the CSV file being imported. </p>"""
    header_list: NotRequired["aws_sdk_dynamodb.types.csv_header_list.CsvHeaderList"]
    """<p> List of the headers used to specify a common header for all source CSV files being imported. If this field is specified then the first line of each CSV file is treated as data instead of the header. If this field is not specified the the first line of each CSV file is treated as the header. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CsvOptions) -> dict:
    out: dict = {}
    if "delimiter" in value:
        out["Delimiter"] = value["delimiter"]
    if "header_list" in value:
        import aws_sdk_dynamodb.types.csv_header_list

        out["HeaderList"] = (
            aws_sdk_dynamodb.types.csv_header_list.serialize_aws_json_1_0(
                value["header_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CsvOptions:
    out: CsvOptions = {}  # type: ignore[typeddict-item]
    if "Delimiter" in data:
        out["delimiter"] = data["Delimiter"]
    if "HeaderList" in data:
        import aws_sdk_dynamodb.types.csv_header_list

        out["header_list"] = (
            aws_sdk_dynamodb.types.csv_header_list.deserialize_aws_json_1_0(
                data["HeaderList"]
            )
        )
    return out
