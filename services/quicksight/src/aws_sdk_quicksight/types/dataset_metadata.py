"""Generated from Smithy shape ``com.amazonaws.quicksight#DatasetMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.data_aggregation
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.topic_calculated_fields
    import aws_sdk_quicksight.types.topic_columns
    import aws_sdk_quicksight.types.topic_filters
    import aws_sdk_quicksight.types.topic_named_entities


class DatasetMetadata(TypedDict, closed=True):
    dataset_arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    dataset_name: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The name of the dataset.</p>"""
    dataset_description: NotRequired[
        "aws_sdk_quicksight.types.limited_string.LimitedString"
    ]
    """<p>The description of the dataset.</p>"""
    data_aggregation: NotRequired[
        "aws_sdk_quicksight.types.data_aggregation.DataAggregation"
    ]
    """<p>The definition of a data aggregation.</p>"""
    filters: NotRequired["aws_sdk_quicksight.types.topic_filters.TopicFilters"]
    """<p>The list of filter definitions.</p>"""
    columns: NotRequired["aws_sdk_quicksight.types.topic_columns.TopicColumns"]
    """<p>The list of column definitions.</p>"""
    calculated_fields: NotRequired[
        "aws_sdk_quicksight.types.topic_calculated_fields.TopicCalculatedFields"
    ]
    """<p>The list of calculated field definitions.</p>"""
    named_entities: NotRequired[
        "aws_sdk_quicksight.types.topic_named_entities.TopicNamedEntities"
    ]
    """<p>The list of named entities definitions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetMetadata) -> dict:
    out: dict = {}
    out["DatasetArn"] = value["dataset_arn"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "dataset_description" in value:
        out["DatasetDescription"] = value["dataset_description"]
    if "data_aggregation" in value:
        import aws_sdk_quicksight.types.data_aggregation

        out["DataAggregation"] = (
            aws_sdk_quicksight.types.data_aggregation.serialize_json(
                value["data_aggregation"]
            )
        )
    if "filters" in value:
        import aws_sdk_quicksight.types.topic_filters

        out["Filters"] = aws_sdk_quicksight.types.topic_filters.serialize_json(
            value["filters"]
        )
    if "columns" in value:
        import aws_sdk_quicksight.types.topic_columns

        out["Columns"] = aws_sdk_quicksight.types.topic_columns.serialize_json(
            value["columns"]
        )
    if "calculated_fields" in value:
        import aws_sdk_quicksight.types.topic_calculated_fields

        out["CalculatedFields"] = (
            aws_sdk_quicksight.types.topic_calculated_fields.serialize_json(
                value["calculated_fields"]
            )
        )
    if "named_entities" in value:
        import aws_sdk_quicksight.types.topic_named_entities

        out["NamedEntities"] = (
            aws_sdk_quicksight.types.topic_named_entities.serialize_json(
                value["named_entities"]
            )
        )
    return out


def deserialize_json(data: dict) -> DatasetMetadata:
    out: DatasetMetadata = {}  # type: ignore[typeddict-item]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        raise DeserializationError("DatasetMetadata.dataset_arn required")
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    if "DatasetDescription" in data:
        out["dataset_description"] = data["DatasetDescription"]
    if "DataAggregation" in data:
        import aws_sdk_quicksight.types.data_aggregation

        out["data_aggregation"] = (
            aws_sdk_quicksight.types.data_aggregation.deserialize_json(
                data["DataAggregation"]
            )
        )
    if "Filters" in data:
        import aws_sdk_quicksight.types.topic_filters

        out["filters"] = aws_sdk_quicksight.types.topic_filters.deserialize_json(
            data["Filters"]
        )
    if "Columns" in data:
        import aws_sdk_quicksight.types.topic_columns

        out["columns"] = aws_sdk_quicksight.types.topic_columns.deserialize_json(
            data["Columns"]
        )
    if "CalculatedFields" in data:
        import aws_sdk_quicksight.types.topic_calculated_fields

        out["calculated_fields"] = (
            aws_sdk_quicksight.types.topic_calculated_fields.deserialize_json(
                data["CalculatedFields"]
            )
        )
    if "NamedEntities" in data:
        import aws_sdk_quicksight.types.topic_named_entities

        out["named_entities"] = (
            aws_sdk_quicksight.types.topic_named_entities.deserialize_json(
                data["NamedEntities"]
            )
        )
    return out
