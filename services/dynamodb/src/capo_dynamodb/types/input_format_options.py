"""Generated from Smithy shape ``com.amazonaws.dynamodb#InputFormatOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.csv_options


class InputFormatOptions(TypedDict, closed=True):
    csv: NotRequired["capo_dynamodb.types.csv_options.CsvOptions"]
    """<p> The options for imported source files in CSV format. The values are Delimiter and HeaderList. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InputFormatOptions) -> dict:
    out: dict = {}
    if "csv" in value:
        import capo_dynamodb.types.csv_options

        out["Csv"] = capo_dynamodb.types.csv_options.serialize_aws_json_1_0(
            value["csv"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InputFormatOptions:
    out: InputFormatOptions = {}  # type: ignore[typeddict-item]
    if data.get("Csv") is not None:
        import capo_dynamodb.types.csv_options

        out["csv"] = capo_dynamodb.types.csv_options.deserialize_aws_json_1_0(
            data["Csv"]
        )
    return out
