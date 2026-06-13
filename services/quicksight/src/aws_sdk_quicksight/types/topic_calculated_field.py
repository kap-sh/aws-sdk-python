"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicCalculatedField``."""

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
    import aws_sdk_quicksight.types.expression
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.nullable_boolean
    import aws_sdk_quicksight.types.semantic_type
    import aws_sdk_quicksight.types.synonyms
    import aws_sdk_quicksight.types.topic_time_granularity


class TopicCalculatedField(TypedDict):
    calculated_field_name: "aws_sdk_quicksight.types.limited_string.LimitedString"
    """<p>The calculated field name.</p>"""
    calculated_field_description: NotRequired[
        "aws_sdk_quicksight.types.limited_string.LimitedString"
    ]
    """<p>The calculated field description.</p>"""
    expression: "aws_sdk_quicksight.types.expression.Expression"
    """<p>The calculated field expression.</p>"""
    calculated_field_synonyms: NotRequired["aws_sdk_quicksight.types.synonyms.Synonyms"]
    """<p>The other names or aliases for the calculated field.</p>"""
    is_included_in_topic: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A boolean value that indicates if a calculated field is included in the topic.</p>"""
    disable_indexing: NotRequired[
        "aws_sdk_quicksight.types.nullable_boolean.NullableBoolean"
    ]
    """<p>A Boolean value that indicates if a calculated field is visible in the autocomplete.</p>"""
    column_data_role: NotRequired[
        "aws_sdk_quicksight.types.column_data_role.ColumnDataRole"
    ]
    """<p>The column data role for a calculated field. Valid values for this structure are <code>DIMENSION</code> and <code>MEASURE</code>.</p>"""
    time_granularity: NotRequired[
        "aws_sdk_quicksight.types.topic_time_granularity.TopicTimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    default_formatting: NotRequired[
        "aws_sdk_quicksight.types.default_formatting.DefaultFormatting"
    ]
    """<p>The default formatting definition.</p>"""
    aggregation: NotRequired[
        "aws_sdk_quicksight.types.default_aggregation.DefaultAggregation"
    ]
    """<p>The default aggregation. Valid values for this structure are <code>SUM</code>, <code>MAX</code>, <code>MIN</code>, <code>COUNT</code>, <code>DISTINCT_COUNT</code>, and <code>AVERAGE</code>.</p>"""
    comparative_order: NotRequired[
        "aws_sdk_quicksight.types.comparative_order.ComparativeOrder"
    ]
    """<p>The order in which data is displayed for the calculated field when it's used in a comparative context.</p>"""
    semantic_type: NotRequired["aws_sdk_quicksight.types.semantic_type.SemanticType"]
    """<p>The semantic type.</p>"""
    allowed_aggregations: NotRequired[
        "aws_sdk_quicksight.types.author_specified_aggregations.AuthorSpecifiedAggregations"
    ]
    """<p>The list of aggregation types that are allowed for the calculated field. Valid values for this structure are <code>COUNT</code>, <code>DISTINCT_COUNT</code>, <code>MIN</code>, <code>MAX</code>, <code>MEDIAN</code>, <code>SUM</code>, <code>AVERAGE</code>, <code>STDEV</code>, <code>STDEVP</code>, <code>VAR</code>, <code>VARP</code>, and <code>PERCENTILE</code>.</p>"""
    not_allowed_aggregations: NotRequired[
        "aws_sdk_quicksight.types.author_specified_aggregations.AuthorSpecifiedAggregations"
    ]
    """<p>The list of aggregation types that are not allowed for the calculated field. Valid values for this structure are <code>COUNT</code>, <code>DISTINCT_COUNT</code>, <code>MIN</code>, <code>MAX</code>, <code>MEDIAN</code>, <code>SUM</code>, <code>AVERAGE</code>, <code>STDEV</code>, <code>STDEVP</code>, <code>VAR</code>, <code>VARP</code>, and <code>PERCENTILE</code>.</p>"""
    never_aggregate_in_filter: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether to never aggregate calculated field in filters.</p>"""
    cell_value_synonyms: NotRequired[
        "aws_sdk_quicksight.types.cell_value_synonyms.CellValueSynonyms"
    ]
    """<p>The other names or aliases for the calculated field cell value.</p>"""
    non_additive: NotRequired[
        "aws_sdk_quicksight.types.nullable_boolean.NullableBoolean"
    ]
    """<p>The non additive for the table style target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicCalculatedField) -> dict:
    out: dict = {}
    out["CalculatedFieldName"] = value["calculated_field_name"]
    if "calculated_field_description" in value:
        out["CalculatedFieldDescription"] = value["calculated_field_description"]
    out["Expression"] = value["expression"]
    if "calculated_field_synonyms" in value:
        import aws_sdk_quicksight.types.synonyms

        out["CalculatedFieldSynonyms"] = (
            aws_sdk_quicksight.types.synonyms.serialize_json(
                value["calculated_field_synonyms"]
            )
        )
    out["IsIncludedInTopic"] = value.get("is_included_in_topic", False)
    if "disable_indexing" in value:
        out["DisableIndexing"] = value["disable_indexing"]
    if "column_data_role" in value:
        import aws_sdk_quicksight.types.column_data_role

        out["ColumnDataRole"] = (
            aws_sdk_quicksight.types.column_data_role.serialize_json(
                value["column_data_role"]
            )
        )
    if "time_granularity" in value:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["TimeGranularity"] = (
            aws_sdk_quicksight.types.topic_time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    if "default_formatting" in value:
        import aws_sdk_quicksight.types.default_formatting

        out["DefaultFormatting"] = (
            aws_sdk_quicksight.types.default_formatting.serialize_json(
                value["default_formatting"]
            )
        )
    if "aggregation" in value:
        import aws_sdk_quicksight.types.default_aggregation

        out["Aggregation"] = (
            aws_sdk_quicksight.types.default_aggregation.serialize_json(
                value["aggregation"]
            )
        )
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


def deserialize_json(data: dict) -> TopicCalculatedField:
    out: TopicCalculatedField = {}  # type: ignore[typeddict-item]
    if "CalculatedFieldName" in data:
        out["calculated_field_name"] = data["CalculatedFieldName"]
    else:
        raise DeserializationError(
            "TopicCalculatedField.calculated_field_name required"
        )
    if "CalculatedFieldDescription" in data:
        out["calculated_field_description"] = data["CalculatedFieldDescription"]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("TopicCalculatedField.expression required")
    if "CalculatedFieldSynonyms" in data:
        import aws_sdk_quicksight.types.synonyms

        out["calculated_field_synonyms"] = (
            aws_sdk_quicksight.types.synonyms.deserialize_json(
                data["CalculatedFieldSynonyms"]
            )
        )
    if "IsIncludedInTopic" in data:
        out["is_included_in_topic"] = data["IsIncludedInTopic"]
    else:
        out["is_included_in_topic"] = False
    if "DisableIndexing" in data:
        out["disable_indexing"] = data["DisableIndexing"]
    if "ColumnDataRole" in data:
        import aws_sdk_quicksight.types.column_data_role

        out["column_data_role"] = (
            aws_sdk_quicksight.types.column_data_role.deserialize_json(
                data["ColumnDataRole"]
            )
        )
    if "TimeGranularity" in data:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["time_granularity"] = (
            aws_sdk_quicksight.types.topic_time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if "DefaultFormatting" in data:
        import aws_sdk_quicksight.types.default_formatting

        out["default_formatting"] = (
            aws_sdk_quicksight.types.default_formatting.deserialize_json(
                data["DefaultFormatting"]
            )
        )
    if "Aggregation" in data:
        import aws_sdk_quicksight.types.default_aggregation

        out["aggregation"] = (
            aws_sdk_quicksight.types.default_aggregation.deserialize_json(
                data["Aggregation"]
            )
        )
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
