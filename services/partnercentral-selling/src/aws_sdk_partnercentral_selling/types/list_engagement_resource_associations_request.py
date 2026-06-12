"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementResourceAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_account
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.page_size
    import aws_sdk_partnercentral_selling.types.resource_identifier
    import aws_sdk_partnercentral_selling.types.resource_type


class ListEngagementResourceAssociationsRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which to search for engagement-resource associations. Valid Values: \"AWS\" or \"Sandbox\"</p> <ul> <li> <p> <code>AWS</code> for production environments.</p> </li> <li> <p> <code>Sandbox</code> for testing and development purposes.</p> </li> </ul>"""
    max_results: "aws_sdk_partnercentral_selling.types.page_size.PageSize"
    """<p>Limits the number of results returned in a single call. Use this to control the number of results returned, especially useful for pagination.</p>"""
    next_token: NotRequired["str"]
    """<p>A token used for pagination of results. Include this token in subsequent requests to retrieve the next set of results.</p>"""
    engagement_identifier: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>Filters the results to include only associations related to the specified engagement. Use this when you want to find all resources associated with a specific engagement.</p>"""
    resource_type: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_type.ResourceType"
    ]
    """<p> Filters the results to include only associations with resources of the specified type. </p>"""
    resource_identifier: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>Filters the results to include only associations with the specified resource. Varies depending on the resource type. Use this when you want to find all engagements associated with a specific resource.</p>"""
    created_by: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
    ]
    """<p>Filters the response to include only snapshots of resources owned by the specified AWS account ID. Use this when you want to find associations related to resources owned by a particular account. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEngagementResourceAssociationsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["MaxResults"] = value.get("max_results", 100)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "engagement_identifier" in value:
        out["EngagementIdentifier"] = value["engagement_identifier"]
    if "resource_type" in value:
        import aws_sdk_partnercentral_selling.types.resource_type

        out["ResourceType"] = (
            aws_sdk_partnercentral_selling.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEngagementResourceAssociationsRequest:
    out: ListEngagementResourceAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError(
            "ListEngagementResourceAssociationsRequest.catalog required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 100
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "EngagementIdentifier" in data:
        out["engagement_identifier"] = data["EngagementIdentifier"]
    if "ResourceType" in data:
        import aws_sdk_partnercentral_selling.types.resource_type

        out["resource_type"] = (
            aws_sdk_partnercentral_selling.types.resource_type.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    if "ResourceIdentifier" in data:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    return out
