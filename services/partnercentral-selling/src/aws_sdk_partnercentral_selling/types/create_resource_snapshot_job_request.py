"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateResourceSnapshotJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.client_token
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.resource_identifier
    import aws_sdk_partnercentral_selling.types.resource_template_name
    import aws_sdk_partnercentral_selling.types.resource_type
    import aws_sdk_partnercentral_selling.types.tag_list


class CreateResourceSnapshotJobRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which to create the snapshot job. Valid values are <code>AWS</code> and <code> Sandbox</code>.</p>"""
    client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken"
    """<p>A client-generated UUID used for idempotency check. The token helps prevent duplicate job creations.</p>"""
    engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    """<p>Specifies the identifier of the engagement associated with the resource to be snapshotted.</p>"""
    resource_type: "aws_sdk_partnercentral_selling.types.resource_type.ResourceType"
    """<p>The type of resource for which the snapshot job is being created. Must be one of the supported resource types i.e. <code>Opportunity</code> </p>"""
    resource_identifier: (
        "aws_sdk_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
    )
    """<p>Specifies the identifier of the specific resource to be snapshotted. The format depends on the <code> ResourceType</code>.</p>"""
    resource_snapshot_template_identifier: "aws_sdk_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
    """<p>Specifies the name of the template that defines the schema for the snapshot.</p>"""
    tags: NotRequired["aws_sdk_partnercentral_selling.types.tag_list.TagList"]
    """<p>A map of the key-value pairs of the tag or tags to assign.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateResourceSnapshotJobRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
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
    if "tags" in value:
        import aws_sdk_partnercentral_selling.types.tag_list

        out["Tags"] = (
            aws_sdk_partnercentral_selling.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateResourceSnapshotJobRequest:
    out: CreateResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("CreateResourceSnapshotJobRequest.catalog required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "CreateResourceSnapshotJobRequest.client_token required"
        )
    if "EngagementIdentifier" in data:
        out["engagement_identifier"] = data["EngagementIdentifier"]
    else:
        raise DeserializationError(
            "CreateResourceSnapshotJobRequest.engagement_identifier required"
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
            "CreateResourceSnapshotJobRequest.resource_type required"
        )
    if "ResourceIdentifier" in data:
        out["resource_identifier"] = data["ResourceIdentifier"]
    else:
        raise DeserializationError(
            "CreateResourceSnapshotJobRequest.resource_identifier required"
        )
    if "ResourceSnapshotTemplateIdentifier" in data:
        out["resource_snapshot_template_identifier"] = data[
            "ResourceSnapshotTemplateIdentifier"
        ]
    else:
        raise DeserializationError(
            "CreateResourceSnapshotJobRequest.resource_snapshot_template_identifier required"
        )
    if "Tags" in data:
        import aws_sdk_partnercentral_selling.types.tag_list

        out["tags"] = (
            aws_sdk_partnercentral_selling.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
