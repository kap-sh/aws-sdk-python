"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Widget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.query_alias
    import aws_sdk_cloudtrail.types.query_parameters
    import aws_sdk_cloudtrail.types.query_statement
    import aws_sdk_cloudtrail.types.view_properties_map


class Widget(TypedDict):
    query_alias: NotRequired["aws_sdk_cloudtrail.types.query_alias.QueryAlias"]
    """<p>The query alias used to identify the query for the widget. </p>"""
    query_statement: NotRequired[
        "aws_sdk_cloudtrail.types.query_statement.QueryStatement"
    ]
    """<p> The SQL query statement for the widget. </p>"""
    query_parameters: NotRequired[
        "aws_sdk_cloudtrail.types.query_parameters.QueryParameters"
    ]
    """<p> The query parameters for the widget. </p>"""
    view_properties: NotRequired[
        "aws_sdk_cloudtrail.types.view_properties_map.ViewPropertiesMap"
    ]
    r"""<p> The view properties for the widget. For more information about view properties, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-widget-properties.html\"> View properties for widgets </a> in the <i>CloudTrail User Guide</i>.. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Widget) -> dict:
    out: dict = {}
    if "query_alias" in value:
        out["QueryAlias"] = value["query_alias"]
    if "query_statement" in value:
        out["QueryStatement"] = value["query_statement"]
    if "query_parameters" in value:
        import aws_sdk_cloudtrail.types.query_parameters

        out["QueryParameters"] = (
            aws_sdk_cloudtrail.types.query_parameters.serialize_aws_json_1_1(
                value["query_parameters"]
            )
        )
    if "view_properties" in value:
        import aws_sdk_cloudtrail.types.view_properties_map

        out["ViewProperties"] = (
            aws_sdk_cloudtrail.types.view_properties_map.serialize_aws_json_1_1(
                value["view_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Widget:
    out: Widget = {}  # type: ignore[typeddict-item]
    if "QueryAlias" in data:
        out["query_alias"] = data["QueryAlias"]
    if "QueryStatement" in data:
        out["query_statement"] = data["QueryStatement"]
    if "QueryParameters" in data:
        import aws_sdk_cloudtrail.types.query_parameters

        out["query_parameters"] = (
            aws_sdk_cloudtrail.types.query_parameters.deserialize_aws_json_1_1(
                data["QueryParameters"]
            )
        )
    if "ViewProperties" in data:
        import aws_sdk_cloudtrail.types.view_properties_map

        out["view_properties"] = (
            aws_sdk_cloudtrail.types.view_properties_map.deserialize_aws_json_1_1(
                data["ViewProperties"]
            )
        )
    return out
