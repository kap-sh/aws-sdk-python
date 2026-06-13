"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#View``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resource_explorer_2.types.included_property_list
    import aws_sdk_resource_explorer_2.types.search_filter
    import aws_sdk_resource_explorer_2.types.view_name


class View(TypedDict):
    view_arn: NotRequired["str"]
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the view.</p>"""
    view_name: NotRequired["aws_sdk_resource_explorer_2.types.view_name.ViewName"]
    """<p>The name of the view.</p>"""
    owner: NotRequired["str"]
    """<p>The Amazon Web Services account that owns this view.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when this view was last modified.</p>"""
    scope: NotRequired["str"]
    """<p>An <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of an Amazon Web Services account, an organization, or an organizational unit (OU) that specifies whether this view includes resources from only the specified Amazon Web Services account, all accounts in the specified organization, or all accounts in the specified OU.</p> <p>If not specified, the value defaults to the Amazon Web Services account used to call this operation.</p>"""
    included_properties: NotRequired[
        "aws_sdk_resource_explorer_2.types.included_property_list.IncludedPropertyList"
    ]
    """<p>A structure that contains additional information about the view.</p>"""
    filters: NotRequired["aws_sdk_resource_explorer_2.types.search_filter.SearchFilter"]
    """<p>An array of <a>SearchFilter</a> objects that specify which resources can be included in the results of queries made using this view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: View) -> dict:
    out: dict = {}
    if "view_arn" in value:
        out["ViewArn"] = value["view_arn"]
    if "view_name" in value:
        out["ViewName"] = value["view_name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "last_updated_at" in value:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["LastUpdatedAt"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    if "scope" in value:
        out["Scope"] = value["scope"]
    if "included_properties" in value:
        import aws_sdk_resource_explorer_2.types.included_property_list

        out["IncludedProperties"] = (
            aws_sdk_resource_explorer_2.types.included_property_list.serialize_json(
                value["included_properties"]
            )
        )
    if "filters" in value:
        import aws_sdk_resource_explorer_2.types.search_filter

        out["Filters"] = aws_sdk_resource_explorer_2.types.search_filter.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> View:
    out: View = {}  # type: ignore[typeddict-item]
    if "ViewArn" in data:
        out["view_arn"] = data["ViewArn"]
    if "ViewName" in data:
        out["view_name"] = data["ViewName"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "LastUpdatedAt" in data:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "Scope" in data:
        out["scope"] = data["Scope"]
    if "IncludedProperties" in data:
        import aws_sdk_resource_explorer_2.types.included_property_list

        out["included_properties"] = (
            aws_sdk_resource_explorer_2.types.included_property_list.deserialize_json(
                data["IncludedProperties"]
            )
        )
    if "Filters" in data:
        import aws_sdk_resource_explorer_2.types.search_filter

        out["filters"] = (
            aws_sdk_resource_explorer_2.types.search_filter.deserialize_json(
                data["Filters"]
            )
        )
    return out
