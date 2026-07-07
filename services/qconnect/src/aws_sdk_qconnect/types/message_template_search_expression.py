"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateSearchExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_filter_field_list
    import aws_sdk_qconnect.types.message_template_order_field
    import aws_sdk_qconnect.types.message_template_query_field_list


class MessageTemplateSearchExpression(TypedDict, closed=True):
    queries: NotRequired[
        "aws_sdk_qconnect.types.message_template_query_field_list.MessageTemplateQueryFieldList"
    ]
    """<p>The message template query expressions.</p>"""
    filters: NotRequired[
        "aws_sdk_qconnect.types.message_template_filter_field_list.MessageTemplateFilterFieldList"
    ]
    """<p>The configuration of filtering rules applied to message template query results.</p>"""
    order_on_field: NotRequired[
        "aws_sdk_qconnect.types.message_template_order_field.MessageTemplateOrderField"
    ]
    """<p>The message template attribute fields on which the query results are ordered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateSearchExpression) -> dict:
    out: dict = {}
    if "queries" in value:
        import aws_sdk_qconnect.types.message_template_query_field_list

        out["queries"] = (
            aws_sdk_qconnect.types.message_template_query_field_list.serialize_json(
                value["queries"]
            )
        )
    if "filters" in value:
        import aws_sdk_qconnect.types.message_template_filter_field_list

        out["filters"] = (
            aws_sdk_qconnect.types.message_template_filter_field_list.serialize_json(
                value["filters"]
            )
        )
    if "order_on_field" in value:
        import aws_sdk_qconnect.types.message_template_order_field

        out["orderOnField"] = (
            aws_sdk_qconnect.types.message_template_order_field.serialize_json(
                value["order_on_field"]
            )
        )
    return out


def deserialize_json(data: dict) -> MessageTemplateSearchExpression:
    out: MessageTemplateSearchExpression = {}  # type: ignore[typeddict-item]
    if "queries" in data:
        import aws_sdk_qconnect.types.message_template_query_field_list

        out["queries"] = (
            aws_sdk_qconnect.types.message_template_query_field_list.deserialize_json(
                data["queries"]
            )
        )
    if "filters" in data:
        import aws_sdk_qconnect.types.message_template_filter_field_list

        out["filters"] = (
            aws_sdk_qconnect.types.message_template_filter_field_list.deserialize_json(
                data["filters"]
            )
        )
    if "orderOnField" in data:
        import aws_sdk_qconnect.types.message_template_order_field

        out["order_on_field"] = (
            aws_sdk_qconnect.types.message_template_order_field.deserialize_json(
                data["orderOnField"]
            )
        )
    return out
