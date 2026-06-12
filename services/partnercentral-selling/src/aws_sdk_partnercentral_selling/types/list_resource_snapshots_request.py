"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListResourceSnapshotsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_account
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.page_size
    import aws_sdk_partnercentral_selling.types.resource_identifier
    import aws_sdk_partnercentral_selling.types.resource_template_name
    import aws_sdk_partnercentral_selling.types.resource_type


class ListResourceSnapshotsRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p> Specifies the catalog related to the request. </p>"""
    max_results: "aws_sdk_partnercentral_selling.types.page_size.PageSize"
    """<p> The maximum number of results to return in a single call. </p>"""
    next_token: NotRequired["str"]
    """<p> The token for the next set of results. </p>"""
    engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    """<p> The unique identifier of the engagement associated with the snapshots. </p>"""
    resource_type: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_type.ResourceType"
    ]
    """<p> Filters the response to include only snapshots of the specified resource type. </p>"""
    resource_identifier: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
    ]
    """<p> Filters the response to include only snapshots of the specified resource. </p>"""
    resource_snapshot_template_identifier: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
    ]
    """<p>Filters the response to include only snapshots created using the specified template.</p>"""
    created_by: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
    ]
    """<p>Filters the response to include only snapshots of resources owned by the specified AWS account. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResourceSnapshotsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["MaxResults"] = value.get("max_results", 100)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
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
    if "resource_snapshot_template_identifier" in value:
        out["ResourceSnapshotTemplateIdentifier"] = value[
            "resource_snapshot_template_identifier"
        ]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListResourceSnapshotsRequest:
    out: ListResourceSnapshotsRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListResourceSnapshotsRequest.catalog required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 100
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "EngagementIdentifier" in data:
        out["engagement_identifier"] = data["EngagementIdentifier"]
    else:
        raise DeserializationError(
            "ListResourceSnapshotsRequest.engagement_identifier required"
        )
    if "ResourceType" in data:
        import aws_sdk_partnercentral_selling.types.resource_type

        out["resource_type"] = (
            aws_sdk_partnercentral_selling.types.resource_type.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    if "ResourceIdentifier" in data:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if "ResourceSnapshotTemplateIdentifier" in data:
        out["resource_snapshot_template_identifier"] = data[
            "ResourceSnapshotTemplateIdentifier"
        ]
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    return out
