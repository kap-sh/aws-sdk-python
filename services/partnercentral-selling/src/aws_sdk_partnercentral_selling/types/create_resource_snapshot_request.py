"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateResourceSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.client_token
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.resource_identifier
    import aws_sdk_partnercentral_selling.types.resource_template_name
    import aws_sdk_partnercentral_selling.types.resource_type


class CreateResourceSnapshotRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p> Specifies the catalog where the snapshot is created. Valid values are <code>AWS</code> and <code>Sandbox</code>. </p>"""
    engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    """<p> The unique identifier of the engagement associated with this snapshot. This field links the snapshot to a specific engagement context. </p>"""
    resource_type: "aws_sdk_partnercentral_selling.types.resource_type.ResourceType"
    """<p> Specifies the type of resource for which the snapshot is being created. This field determines the structure and content of the snapshot. Must be one of the supported resource types, such as: <code>Opportunity</code>. </p>"""
    resource_identifier: (
        "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
    )
    """<p> The unique identifier of the specific resource to be snapshotted. The format and constraints of this identifier depend on the <code>ResourceType</code> specified. For example: For <code>Opportunity</code> type, it will be an opportunity ID. </p>"""
    resource_snapshot_template_identifier: "aws_sdk_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
    """<p> The name of the template that defines the schema for the snapshot. This template determines which subset of the resource data will be included in the snapshot. Must correspond to an existing and valid template for the specified <code>ResourceType</code>. </p>"""
    client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken"
    """<p> Specifies a unique, client-generated UUID to ensure that the request is handled exactly once. This token helps prevent duplicate snapshot creations. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateResourceSnapshotRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["EngagementIdentifier"] = value["engagement_identifier"]
    import aws_sdk_partnercentral_selling.types.resource_type

    out["ResourceType"] = (
        aws_sdk_partnercentral_selling.types.resource_type.serialize_aws_json_1_0(
            value["resource_type"]
        )
    )
    out["ResourceIdentifier"] = value["resource_identifier"]
    out["ResourceSnapshotTemplateIdentifier"] = value[
        "resource_snapshot_template_identifier"
    ]
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateResourceSnapshotRequest:
    out: CreateResourceSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("CreateResourceSnapshotRequest.catalog required")
    if "EngagementIdentifier" in data:
        out["engagement_identifier"] = data["EngagementIdentifier"]
    else:
        raise DeserializationError(
            "CreateResourceSnapshotRequest.engagement_identifier required"
        )
    if "ResourceType" in data:
        import aws_sdk_partnercentral_selling.types.resource_type

        out["resource_type"] = (
            aws_sdk_partnercentral_selling.types.resource_type.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateResourceSnapshotRequest.resource_type required"
        )
    if "ResourceIdentifier" in data:
        out["resource_identifier"] = data["ResourceIdentifier"]
    else:
        raise DeserializationError(
            "CreateResourceSnapshotRequest.resource_identifier required"
        )
    if "ResourceSnapshotTemplateIdentifier" in data:
        out["resource_snapshot_template_identifier"] = data[
            "ResourceSnapshotTemplateIdentifier"
        ]
    else:
        raise DeserializationError(
            "CreateResourceSnapshotRequest.resource_snapshot_template_identifier required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "CreateResourceSnapshotRequest.client_token required"
        )
    return out
