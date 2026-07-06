"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#CreateViewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resource_explorer_2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.included_property_list
    import aws_sdk_resource_explorer_2.types.search_filter
    import aws_sdk_resource_explorer_2.types.tag_map
    import aws_sdk_resource_explorer_2.types.view_name


class CreateViewInput(TypedDict, closed=True):
    client_token: NotRequired["str"]
    r"""<p>This value helps ensure idempotency. Resource Explorer uses this value to prevent the accidental creation of duplicate versions. We recommend that you generate a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID-type value</a> to ensure the uniqueness of your views.</p>"""
    view_name: "aws_sdk_resource_explorer_2.types.view_name.ViewName"
    """<p>The name of the new view. This name appears in the list of views in Resource Explorer.</p> <p>The name must be no more than 64 characters long, and can include letters, digits, and the dash (-) character. The name must be unique within its Amazon Web Services Region.</p>"""
    included_properties: NotRequired[
        "aws_sdk_resource_explorer_2.types.included_property_list.IncludedPropertyList"
    ]
    """<p>Specifies optional fields that you want included in search results from this view. It is a list of objects that each describe a field to include.</p> <p>The default is an empty list, with no optional fields included in the results.</p>"""
    scope: NotRequired["str"]
    """<p>The root ARN of the account, an organizational unit (OU), or an organization ARN. If left empty, the default is account.</p>"""
    filters: NotRequired["aws_sdk_resource_explorer_2.types.search_filter.SearchFilter"]
    r"""<p>An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a <a>Search</a> operation, the filter string is combined with the search's <code>QueryString</code> parameter using a logical <code>AND</code> operator.</p> <p>For information about the supported syntax, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html\">Search query reference for Resource Explorer</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <important> <p>This query string in the context of this operation supports only <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters\">filter prefixes</a> with optional <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators\">operators</a>. It doesn't support free-form text. For example, the string <code>region:us* service:ec2 -tag:stage=prod</code> includes all Amazon EC2 resources in any Amazon Web Services Region that begins with the letters <code>us</code> and is <i>not</i> tagged with a key <code>Stage</code> that has the value <code>prod</code>.</p> </important>"""
    tags: NotRequired["aws_sdk_resource_explorer_2.types.tag_map.TagMap"]
    """<p>Tag key and value pairs that are attached to the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateViewInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["ViewName"] = value["view_name"]
    if "included_properties" in value:
        import aws_sdk_resource_explorer_2.types.included_property_list

        out["IncludedProperties"] = (
            aws_sdk_resource_explorer_2.types.included_property_list.serialize_json(
                value["included_properties"]
            )
        )
    if "scope" in value:
        out["Scope"] = value["scope"]
    if "filters" in value:
        import aws_sdk_resource_explorer_2.types.search_filter

        out["Filters"] = aws_sdk_resource_explorer_2.types.search_filter.serialize_json(
            value["filters"]
        )
    if "tags" in value:
        import aws_sdk_resource_explorer_2.types.tag_map

        out["Tags"] = aws_sdk_resource_explorer_2.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateViewInput:
    out: CreateViewInput = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ViewName" in data:
        out["view_name"] = data["ViewName"]
    else:
        raise DeserializationError("CreateViewInput.view_name required")
    if "IncludedProperties" in data:
        import aws_sdk_resource_explorer_2.types.included_property_list

        out["included_properties"] = (
            aws_sdk_resource_explorer_2.types.included_property_list.deserialize_json(
                data["IncludedProperties"]
            )
        )
    if "Scope" in data:
        out["scope"] = data["Scope"]
    if "Filters" in data:
        import aws_sdk_resource_explorer_2.types.search_filter

        out["filters"] = (
            aws_sdk_resource_explorer_2.types.search_filter.deserialize_json(
                data["Filters"]
            )
        )
    if "Tags" in data:
        import aws_sdk_resource_explorer_2.types.tag_map

        out["tags"] = aws_sdk_resource_explorer_2.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
