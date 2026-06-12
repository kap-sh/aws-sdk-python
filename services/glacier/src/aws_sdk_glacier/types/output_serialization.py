"""Generated from Smithy shape ``com.amazonaws.glacier#OutputSerialization``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.csv_output


class OutputSerialization(TypedDict):
    csv: NotRequired["aws_sdk_glacier.types.csv_output.CSVOutput"]
    """<p>Describes the serialization of CSV-encoded query results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputSerialization) -> dict:
    out: dict = {}
    if "csv" in value:
        import aws_sdk_glacier.types.csv_output

        out["csv"] = aws_sdk_glacier.types.csv_output.serialize_json(value["csv"])
    return out


def deserialize_json(data: dict) -> OutputSerialization:
    out: OutputSerialization = {}  # type: ignore[typeddict-item]
    if "csv" in data:
        import aws_sdk_glacier.types.csv_output

        out["csv"] = aws_sdk_glacier.types.csv_output.deserialize_json(data["csv"])
    return out
