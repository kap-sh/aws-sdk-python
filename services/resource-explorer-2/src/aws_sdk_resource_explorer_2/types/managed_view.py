"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ManagedView``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resource_explorer_2.types.included_property_list
    import aws_sdk_resource_explorer_2.types.search_filter


class ManagedView(TypedDict):
    managed_view_arn: NotRequired["str"]
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the managed view.</p>"""
    managed_view_name: NotRequired["str"]
    """<p>The name of the managed view. </p>"""
    trusted_service: NotRequired["str"]
    """<p>The service principal of the Amazon Web Services service that created and manages the managed view. </p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when this managed view was last modified.</p>"""
    owner: NotRequired["str"]
    """<p>The Amazon Web Services account that owns this managed view.</p>"""
    scope: NotRequired["str"]
    """<p>An <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of an Amazon Web Services account or organization that specifies whether this managed view includes resources from only the specified Amazon Web Services account or all accounts in the specified organization. </p>"""
    included_properties: NotRequired[
        "aws_sdk_resource_explorer_2.types.included_property_list.IncludedPropertyList"
    ]
    """<p>A structure that contains additional information about the managed view.</p>"""
    filters: NotRequired["aws_sdk_resource_explorer_2.types.search_filter.SearchFilter"]
    resource_policy: NotRequired["str"]
    """<p>The resource policy that defines access to the managed view. To learn more about this policy, review <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html\">Managed views</a>.</p>"""
    version: NotRequired["str"]
    """<p>The version of the managed view. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedView) -> dict:
    out: dict = {}
    if "managed_view_arn" in value:
        out["ManagedViewArn"] = value["managed_view_arn"]
    if "managed_view_name" in value:
        out["ManagedViewName"] = value["managed_view_name"]
    if "trusted_service" in value:
        out["TrustedService"] = value["trusted_service"]
    if "last_updated_at" in value:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["LastUpdatedAt"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
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
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ManagedView:
    out: ManagedView = {}  # type: ignore[typeddict-item]
    if "ManagedViewArn" in data:
        out["managed_view_arn"] = data["ManagedViewArn"]
    if "ManagedViewName" in data:
        out["managed_view_name"] = data["ManagedViewName"]
    if "TrustedService" in data:
        out["trusted_service"] = data["TrustedService"]
    if "LastUpdatedAt" in data:
        import aws_sdk_resource_explorer_2.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_resource_explorer_2.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "Owner" in data:
        out["owner"] = data["Owner"]
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
    if "ResourcePolicy" in data:
        out["resource_policy"] = data["ResourcePolicy"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
