"""Generated from Smithy shape ``com.amazonaws.glue#CatalogKinesisSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.boxed_boolean
    import capo_glue.types.boxed_positive_int
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.kinesis_streaming_source_options
    import capo_glue.types.node_name
    import capo_glue.types.streaming_data_preview_options


class CatalogKinesisSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the data source.</p>"""
    window_size: NotRequired["capo_glue.types.boxed_positive_int.BoxedPositiveInt"]
    """<p>The amount of time to spend processing each micro batch.</p>"""
    detect_schema: NotRequired["capo_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Whether to automatically determine the schema from the incoming data.</p>"""
    table: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to read from.</p>"""
    database: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to read from.</p>"""
    streaming_options: NotRequired[
        "capo_glue.types.kinesis_streaming_source_options.KinesisStreamingSourceOptions"
    ]
    """<p>Additional options for the Kinesis streaming data source.</p>"""
    data_preview_options: NotRequired[
        "capo_glue.types.streaming_data_preview_options.StreamingDataPreviewOptions"
    ]
    """<p>Additional options for data preview.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogKinesisSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "window_size" in value:
        out["WindowSize"] = value["window_size"]
    if "detect_schema" in value:
        out["DetectSchema"] = value["detect_schema"]
    out["Table"] = value["table"]
    out["Database"] = value["database"]
    if "streaming_options" in value:
        import capo_glue.types.kinesis_streaming_source_options

        out["StreamingOptions"] = (
            capo_glue.types.kinesis_streaming_source_options.serialize_aws_json_1_1(
                value["streaming_options"]
            )
        )
    if "data_preview_options" in value:
        import capo_glue.types.streaming_data_preview_options

        out["DataPreviewOptions"] = (
            capo_glue.types.streaming_data_preview_options.serialize_aws_json_1_1(
                value["data_preview_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogKinesisSource:
    out: CatalogKinesisSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CatalogKinesisSource.name required")
    if "WindowSize" in data:
        out["window_size"] = data["WindowSize"]
    if "DetectSchema" in data:
        out["detect_schema"] = data["DetectSchema"]
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("CatalogKinesisSource.table required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("CatalogKinesisSource.database required")
    if "StreamingOptions" in data:
        import capo_glue.types.kinesis_streaming_source_options

        out["streaming_options"] = (
            capo_glue.types.kinesis_streaming_source_options.deserialize_aws_json_1_1(
                data["StreamingOptions"]
            )
        )
    if "DataPreviewOptions" in data:
        import capo_glue.types.streaming_data_preview_options

        out["data_preview_options"] = (
            capo_glue.types.streaming_data_preview_options.deserialize_aws_json_1_1(
                data["DataPreviewOptions"]
            )
        )
    return out
