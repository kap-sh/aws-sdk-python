"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ServiceView``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resource_explorer_2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.included_property_list
    import aws_sdk_resource_explorer_2.types.search_filter
    import aws_sdk_resource_explorer_2.types.service_view_name


class ServiceView(TypedDict):
    service_view_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the service view.</p>"""
    service_view_name: NotRequired[
        "aws_sdk_resource_explorer_2.types.service_view_name.ServiceViewName"
    ]
    """<p>The name of the service view.</p>"""
    filters: NotRequired["aws_sdk_resource_explorer_2.types.search_filter.SearchFilter"]
    included_properties: NotRequired[
        "aws_sdk_resource_explorer_2.types.included_property_list.IncludedPropertyList"
    ]
    """<p>A list of additional resource properties that are included in this view for search and filtering purposes.</p>"""
    streaming_access_for_service: NotRequired["str"]
    """<p>The Amazon Web Services service that has streaming access to this view's data.</p>"""
    scope_type: NotRequired["str"]
    """<p>The scope type of the service view, which determines what resources are included.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceView) -> dict:
    out: dict = {}
    out["ServiceViewArn"] = value["service_view_arn"]
    if "service_view_name" in value:
        out["ServiceViewName"] = value["service_view_name"]
    if "filters" in value:
        import aws_sdk_resource_explorer_2.types.search_filter

        out["Filters"] = aws_sdk_resource_explorer_2.types.search_filter.serialize_json(
            value["filters"]
        )
    if "included_properties" in value:
        import aws_sdk_resource_explorer_2.types.included_property_list

        out["IncludedProperties"] = (
            aws_sdk_resource_explorer_2.types.included_property_list.serialize_json(
                value["included_properties"]
            )
        )
    if "streaming_access_for_service" in value:
        out["StreamingAccessForService"] = value["streaming_access_for_service"]
    if "scope_type" in value:
        out["ScopeType"] = value["scope_type"]
    return out


def deserialize_json(data: dict) -> ServiceView:
    out: ServiceView = {}  # type: ignore[typeddict-item]
    if "ServiceViewArn" in data:
        out["service_view_arn"] = data["ServiceViewArn"]
    else:
        raise DeserializationError("ServiceView.service_view_arn required")
    if "ServiceViewName" in data:
        out["service_view_name"] = data["ServiceViewName"]
    if "Filters" in data:
        import aws_sdk_resource_explorer_2.types.search_filter

        out["filters"] = (
            aws_sdk_resource_explorer_2.types.search_filter.deserialize_json(
                data["Filters"]
            )
        )
    if "IncludedProperties" in data:
        import aws_sdk_resource_explorer_2.types.included_property_list

        out["included_properties"] = (
            aws_sdk_resource_explorer_2.types.included_property_list.deserialize_json(
                data["IncludedProperties"]
            )
        )
    if "StreamingAccessForService" in data:
        out["streaming_access_for_service"] = data["StreamingAccessForService"]
    if "ScopeType" in data:
        out["scope_type"] = data["ScopeType"]
    return out
