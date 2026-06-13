"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicColumn``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.author_specified_aggregations
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.cell_value_synonyms
    import aws_sdk_quicksight.types.column_data_role
    import aws_sdk_quicksight.types.comparative_order
    import aws_sdk_quicksight.types.default_aggregation
    import aws_sdk_quicksight.types.default_formatting
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.nullable_boolean
    import aws_sdk_quicksight.types.semantic_type
    import aws_sdk_quicksight.types.synonyms
    import aws_sdk_quicksight.types.topic_time_granularity


class TopicColumn(TypedDict):
    column_name: "aws_sdk_quicksight.types.limited_string.LimitedString"
    """<p>The name of the column.</p>"""
    column_friendly_name: NotRequired[
        "aws_sdk_quicksight.types.limited_string.LimitedString"
    ]
    """<p>A user-friendly name for the column.</p>"""
    column_description: NotRequired[
        "aws_sdk_quicksight.types.limited_string.LimitedString"
    ]
    """<p>A description of the column and its contents.</p>"""
    column_synonyms: NotRequired["aws_sdk_quicksight.types.synonyms.Synonyms"]
    """<p>The other names or aliases for the column.</p>"""
    column_data_role: NotRequired[
        "aws_sdk_quicksight.types.column_data_role.ColumnDataRole"
    ]
    """<p>The role of the column in the data. Valid values are <code>DIMENSION</code> and <code>MEASURE</code>.</p>"""
    aggregation: NotRequired[
        "aws_sdk_quicksight.types.default_aggregation.DefaultAggregation"
    ]
    """<p>The type of aggregation that is performed on the column data when it's queried.</p>"""
    is_included_in_topic: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether the column is included in the query results.</p>"""
    disable_indexing: NotRequired[
        "aws_sdk_quicksight.types.nullable_boolean.NullableBoolean"
    ]
    """<p>A Boolean value that indicates whether the column shows in the autocomplete functionality.</p>"""
    comparative_order: NotRequired[
        "aws_sdk_quicksight.types.comparative_order.ComparativeOrder"
    ]
    """<p>The order in which data is displayed for the column when it's used in a comparative context.</p>"""
    semantic_type: NotRequired["aws_sdk_quicksight.types.semantic_type.SemanticType"]
    """<p>The semantic type of data contained in the column.</p>"""
    time_granularity: NotRequired[
        "aws_sdk_quicksight.types.topic_time_granularity.TopicTimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    allowed_aggregations: NotRequired[
        "aws_sdk_quicksight.types.author_specified_aggregations.AuthorSpecifiedAggregations"
    ]
    """<p>The list of aggregation types that are allowed for the column. Valid values for this structure are <code>COUNT</code>, <code>DISTINCT_COUNT</code>, <code>MIN</code>, <code>MAX</code>, <code>MEDIAN</code>, <code>SUM</code>, <code>AVERAGE</code>, <code>STDEV</code>, <code>STDEVP</code>, <code>VAR</code>, <code>VARP</code>, and <code>PERCENTILE</code>.</p>"""
    not_allowed_aggregations: NotRequired[
        "aws_sdk_quicksight.types.author_specified_aggregations.AuthorSpecifiedAggregations"
    ]
    """<p>The list of aggregation types that are not allowed for the column. Valid values for this structure are <code>COUNT</code>, <code>DISTINCT_COUNT</code>, <code>MIN</code>, <code>MAX</code>, <code>MEDIAN</code>, <code>SUM</code>, <code>AVERAGE</code>, <code>STDEV</code>, <code>STDEVP</code>, <code>VAR</code>, <code>VARP</code>, and <code>PERCENTILE</code>.</p>"""
    default_formatting: NotRequired[
        "aws_sdk_quicksight.types.default_formatting.DefaultFormatting"
    ]
    """<p>The default formatting used for values in the column.</p>"""
    never_aggregate_in_filter: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether to aggregate the column data when it's used in a filter context.</p>"""
    cell_value_synonyms: NotRequired[
        "aws_sdk_quicksight.types.cell_value_synonyms.CellValueSynonyms"
    ]
    """<p>The other names or aliases for the column cell value.</p>"""
    non_additive: NotRequired[
        "aws_sdk_quicksight.types.nullable_boolean.NullableBoolean"
    ]
    """<p>The non additive value for the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicColumn) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    if "column_friendly_name" in value:
        out["ColumnFriendlyName"] = value["column_friendly_name"]
    if "column_description" in value:
        out["ColumnDescription"] = value["column_description"]
    if "column_synonyms" in value:
        import aws_sdk_quicksight.types.synonyms

        out["ColumnSynonyms"] = aws_sdk_quicksight.types.synonyms.serialize_json(
            value["column_synonyms"]
        )
    if "column_data_role" in value:
        import aws_sdk_quicksight.types.column_data_role

        out["ColumnDataRole"] = (
            aws_sdk_quicksight.types.column_data_role.serialize_json(
                value["column_data_role"]
            )
        )
    if "aggregation" in value:
        import aws_sdk_quicksight.types.default_aggregation

        out["Aggregation"] = (
            aws_sdk_quicksight.types.default_aggregation.serialize_json(
                value["aggregation"]
            )
        )
    out["IsIncludedInTopic"] = value.get("is_included_in_topic", False)
    if "disable_indexing" in value:
        out["DisableIndexing"] = value["disable_indexing"]
    if "comparative_order" in value:
        import aws_sdk_quicksight.types.comparative_order

        out["ComparativeOrder"] = (
            aws_sdk_quicksight.types.comparative_order.serialize_json(
                value["comparative_order"]
            )
        )
    if "semantic_type" in value:
        import aws_sdk_quicksight.types.semantic_type

        out["SemanticType"] = aws_sdk_quicksight.types.semantic_type.serialize_json(
            value["semantic_type"]
        )
    if "time_granularity" in value:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["TimeGranularity"] = (
            aws_sdk_quicksight.types.topic_time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    if "allowed_aggregations" in value:
        import aws_sdk_quicksight.types.author_specified_aggregations

        out["AllowedAggregations"] = (
            aws_sdk_quicksight.types.author_specified_aggregations.serialize_json(
                value["allowed_aggregations"]
            )
        )
    if "not_allowed_aggregations" in value:
        import aws_sdk_quicksight.types.author_specified_aggregations

        out["NotAllowedAggregations"] = (
            aws_sdk_quicksight.types.author_specified_aggregations.serialize_json(
                value["not_allowed_aggregations"]
            )
        )
    if "default_formatting" in value:
        import aws_sdk_quicksight.types.default_formatting

        out["DefaultFormatting"] = (
            aws_sdk_quicksight.types.default_formatting.serialize_json(
                value["default_formatting"]
            )
        )
    out["NeverAggregateInFilter"] = value.get("never_aggregate_in_filter", False)
    if "cell_value_synonyms" in value:
        import aws_sdk_quicksight.types.cell_value_synonyms

        out["CellValueSynonyms"] = (
            aws_sdk_quicksight.types.cell_value_synonyms.serialize_json(
                value["cell_value_synonyms"]
            )
        )
    if "non_additive" in value:
        out["NonAdditive"] = value["non_additive"]
    return out


def deserialize_json(data: dict) -> TopicColumn:
    out: TopicColumn = {}  # type: ignore[typeddict-item]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    else:
        raise DeserializationError("TopicColumn.column_name required")
    if "ColumnFriendlyName" in data:
        out["column_friendly_name"] = data["ColumnFriendlyName"]
    if "ColumnDescription" in data:
        out["column_description"] = data["ColumnDescription"]
    if "ColumnSynonyms" in data:
        import aws_sdk_quicksight.types.synonyms

        out["column_synonyms"] = aws_sdk_quicksight.types.synonyms.deserialize_json(
            data["ColumnSynonyms"]
        )
    if "ColumnDataRole" in data:
        import aws_sdk_quicksight.types.column_data_role

        out["column_data_role"] = (
            aws_sdk_quicksight.types.column_data_role.deserialize_json(
                data["ColumnDataRole"]
            )
        )
    if "Aggregation" in data:
        import aws_sdk_quicksight.types.default_aggregation

        out["aggregation"] = (
            aws_sdk_quicksight.types.default_aggregation.deserialize_json(
                data["Aggregation"]
            )
        )
    if "IsIncludedInTopic" in data:
        out["is_included_in_topic"] = data["IsIncludedInTopic"]
    else:
        out["is_included_in_topic"] = False
    if "DisableIndexing" in data:
        out["disable_indexing"] = data["DisableIndexing"]
    if "ComparativeOrder" in data:
        import aws_sdk_quicksight.types.comparative_order

        out["comparative_order"] = (
            aws_sdk_quicksight.types.comparative_order.deserialize_json(
                data["ComparativeOrder"]
            )
        )
    if "SemanticType" in data:
        import aws_sdk_quicksight.types.semantic_type

        out["semantic_type"] = aws_sdk_quicksight.types.semantic_type.deserialize_json(
            data["SemanticType"]
        )
    if "TimeGranularity" in data:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["time_granularity"] = (
            aws_sdk_quicksight.types.topic_time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if "AllowedAggregations" in data:
        import aws_sdk_quicksight.types.author_specified_aggregations

        out["allowed_aggregations"] = (
            aws_sdk_quicksight.types.author_specified_aggregations.deserialize_json(
                data["AllowedAggregations"]
            )
        )
    if "NotAllowedAggregations" in data:
        import aws_sdk_quicksight.types.author_specified_aggregations

        out["not_allowed_aggregations"] = (
            aws_sdk_quicksight.types.author_specified_aggregations.deserialize_json(
                data["NotAllowedAggregations"]
            )
        )
    if "DefaultFormatting" in data:
        import aws_sdk_quicksight.types.default_formatting

        out["default_formatting"] = (
            aws_sdk_quicksight.types.default_formatting.deserialize_json(
                data["DefaultFormatting"]
            )
        )
    if "NeverAggregateInFilter" in data:
        out["never_aggregate_in_filter"] = data["NeverAggregateInFilter"]
    else:
        out["never_aggregate_in_filter"] = False
    if "CellValueSynonyms" in data:
        import aws_sdk_quicksight.types.cell_value_synonyms

        out["cell_value_synonyms"] = (
            aws_sdk_quicksight.types.cell_value_synonyms.deserialize_json(
                data["CellValueSynonyms"]
            )
        )
    if "NonAdditive" in data:
        out["non_additive"] = data["NonAdditive"]
    return out
