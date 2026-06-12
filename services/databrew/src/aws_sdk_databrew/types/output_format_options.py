"""Generated from Smithy shape ``com.amazonaws.databrew#OutputFormatOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_databrew.types.csv_output_options


class OutputFormatOptions(TypedDict):
    csv: NotRequired["aws_sdk_databrew.types.csv_output_options.CsvOutputOptions"]
    """<p>Represents a set of options that define the structure of comma-separated value (CSV) job output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputFormatOptions) -> dict:
    out: dict = {}
    if "csv" in value:
        import aws_sdk_databrew.types.csv_output_options

        out["Csv"] = aws_sdk_databrew.types.csv_output_options.serialize_json(
            value["csv"]
        )
    return out


def deserialize_json(data: dict) -> OutputFormatOptions:
    out: OutputFormatOptions = {}  # type: ignore[typeddict-item]
    if "Csv" in data:
        import aws_sdk_databrew.types.csv_output_options

        out["csv"] = aws_sdk_databrew.types.csv_output_options.deserialize_json(
            data["Csv"]
        )
    return out
