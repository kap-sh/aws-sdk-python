"""Generated from Smithy shape ``com.amazonaws.forecast#TimeSeriesIdentifiers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.data_source
    import capo_forecast.types.format
    import capo_forecast.types.schema


class TimeSeriesIdentifiers(TypedDict, closed=True):
    data_source: NotRequired["capo_forecast.types.data_source.DataSource"]
    schema: NotRequired["capo_forecast.types.schema.Schema"]
    format: NotRequired["capo_forecast.types.format.Format"]
    """<p>The format of the data, either CSV or PARQUET.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeSeriesIdentifiers) -> dict:
    out: dict = {}
    if "data_source" in value:
        import capo_forecast.types.data_source

        out["DataSource"] = capo_forecast.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "schema" in value:
        import capo_forecast.types.schema

        out["Schema"] = capo_forecast.types.schema.serialize_aws_json_1_1(
            value["schema"]
        )
    if "format" in value:
        out["Format"] = value["format"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeSeriesIdentifiers:
    out: TimeSeriesIdentifiers = {}  # type: ignore[typeddict-item]
    if "DataSource" in data:
        import capo_forecast.types.data_source

        out["data_source"] = capo_forecast.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if "Schema" in data:
        import capo_forecast.types.schema

        out["schema"] = capo_forecast.types.schema.deserialize_aws_json_1_1(
            data["Schema"]
        )
    if "Format" in data:
        out["format"] = data["Format"]
    return out
