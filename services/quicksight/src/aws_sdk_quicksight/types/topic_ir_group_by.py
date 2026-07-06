"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRGroupBy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.display_format
    import aws_sdk_quicksight.types.display_format_options
    import aws_sdk_quicksight.types.identifier
    import aws_sdk_quicksight.types.named_entity_ref
    import aws_sdk_quicksight.types.topic_sort_clause
    import aws_sdk_quicksight.types.topic_time_granularity


class TopicIRGroupBy(TypedDict, closed=True):
    field_name: NotRequired["aws_sdk_quicksight.types.identifier.Identifier"]
    """<p>The field name for the <code>TopicIRGroupBy</code>.</p>"""
    time_granularity: NotRequired[
        "aws_sdk_quicksight.types.topic_time_granularity.TopicTimeGranularity"
    ]
    """<p>The time granularity for the <code>TopicIRGroupBy</code>.</p>"""
    sort: NotRequired["aws_sdk_quicksight.types.topic_sort_clause.TopicSortClause"]
    """<p>The sort for the <code>TopicIRGroupBy</code>.</p>"""
    display_format: NotRequired["aws_sdk_quicksight.types.display_format.DisplayFormat"]
    """<p>The display format for the <code>TopicIRGroupBy</code>.</p>"""
    display_format_options: NotRequired[
        "aws_sdk_quicksight.types.display_format_options.DisplayFormatOptions"
    ]
    named_entity: NotRequired[
        "aws_sdk_quicksight.types.named_entity_ref.NamedEntityRef"
    ]
    """<p>The named entity for the <code>TopicIRGroupBy</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRGroupBy) -> dict:
    out: dict = {}
    if "field_name" in value:
        import aws_sdk_quicksight.types.identifier

        out["FieldName"] = aws_sdk_quicksight.types.identifier.serialize_json(
            value["field_name"]
        )
    if "time_granularity" in value:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["TimeGranularity"] = (
            aws_sdk_quicksight.types.topic_time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    if "sort" in value:
        import aws_sdk_quicksight.types.topic_sort_clause

        out["Sort"] = aws_sdk_quicksight.types.topic_sort_clause.serialize_json(
            value["sort"]
        )
    if "display_format" in value:
        import aws_sdk_quicksight.types.display_format

        out["DisplayFormat"] = aws_sdk_quicksight.types.display_format.serialize_json(
            value["display_format"]
        )
    if "display_format_options" in value:
        import aws_sdk_quicksight.types.display_format_options

        out["DisplayFormatOptions"] = (
            aws_sdk_quicksight.types.display_format_options.serialize_json(
                value["display_format_options"]
            )
        )
    if "named_entity" in value:
        import aws_sdk_quicksight.types.named_entity_ref

        out["NamedEntity"] = aws_sdk_quicksight.types.named_entity_ref.serialize_json(
            value["named_entity"]
        )
    return out


def deserialize_json(data: dict) -> TopicIRGroupBy:
    out: TopicIRGroupBy = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        import aws_sdk_quicksight.types.identifier

        out["field_name"] = aws_sdk_quicksight.types.identifier.deserialize_json(
            data["FieldName"]
        )
    if "TimeGranularity" in data:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["time_granularity"] = (
            aws_sdk_quicksight.types.topic_time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if "Sort" in data:
        import aws_sdk_quicksight.types.topic_sort_clause

        out["sort"] = aws_sdk_quicksight.types.topic_sort_clause.deserialize_json(
            data["Sort"]
        )
    if "DisplayFormat" in data:
        import aws_sdk_quicksight.types.display_format

        out["display_format"] = (
            aws_sdk_quicksight.types.display_format.deserialize_json(
                data["DisplayFormat"]
            )
        )
    if "DisplayFormatOptions" in data:
        import aws_sdk_quicksight.types.display_format_options

        out["display_format_options"] = (
            aws_sdk_quicksight.types.display_format_options.deserialize_json(
                data["DisplayFormatOptions"]
            )
        )
    if "NamedEntity" in data:
        import aws_sdk_quicksight.types.named_entity_ref

        out["named_entity"] = (
            aws_sdk_quicksight.types.named_entity_ref.deserialize_json(
                data["NamedEntity"]
            )
        )
    return out
