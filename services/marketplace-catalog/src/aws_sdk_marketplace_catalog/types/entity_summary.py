"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#EntitySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.ami_product_summary
    import aws_sdk_marketplace_catalog.types.arn
    import aws_sdk_marketplace_catalog.types.container_product_summary
    import aws_sdk_marketplace_catalog.types.data_product_summary
    import aws_sdk_marketplace_catalog.types.date_time_iso8601
    import aws_sdk_marketplace_catalog.types.entity_name_string
    import aws_sdk_marketplace_catalog.types.entity_type
    import aws_sdk_marketplace_catalog.types.machine_learning_product_summary
    import aws_sdk_marketplace_catalog.types.offer_set_summary
    import aws_sdk_marketplace_catalog.types.offer_summary
    import aws_sdk_marketplace_catalog.types.resale_authorization_summary
    import aws_sdk_marketplace_catalog.types.resource_id
    import aws_sdk_marketplace_catalog.types.saa_s_product_summary
    import aws_sdk_marketplace_catalog.types.visibility_value


class EntitySummary(TypedDict):
    name: NotRequired[
        "aws_sdk_marketplace_catalog.types.entity_name_string.EntityNameString"
    ]
    """<p>The name for the entity. This value is not unique. It is defined by the seller.</p>"""
    entity_type: NotRequired["aws_sdk_marketplace_catalog.types.entity_type.EntityType"]
    """<p>The type of the entity.</p>"""
    entity_id: NotRequired["aws_sdk_marketplace_catalog.types.resource_id.ResourceId"]
    """<p>The unique identifier for the entity.</p>"""
    entity_arn: NotRequired["aws_sdk_marketplace_catalog.types.arn.ARN"]
    """<p>The ARN associated with the unique identifier for the entity.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The last time the entity was published, using ISO 8601 format (2018-02-27T13:45:22Z).</p>"""
    visibility: NotRequired[
        "aws_sdk_marketplace_catalog.types.visibility_value.VisibilityValue"
    ]
    """<p>The visibility status of the entity to buyers. This value can be <code>Public</code> (everyone can view the entity), <code>Limited</code> (the entity is visible to limited accounts only), or <code>Restricted</code> (the entity was published and then unpublished and only existing buyers can view it). </p>"""
    ami_product_summary: NotRequired[
        "aws_sdk_marketplace_catalog.types.ami_product_summary.AmiProductSummary"
    ]
    """<p>An object that contains summary information about the AMI product.</p>"""
    container_product_summary: NotRequired[
        "aws_sdk_marketplace_catalog.types.container_product_summary.ContainerProductSummary"
    ]
    """<p>An object that contains summary information about the container product.</p>"""
    data_product_summary: NotRequired[
        "aws_sdk_marketplace_catalog.types.data_product_summary.DataProductSummary"
    ]
    """<p>An object that contains summary information about the data product.</p>"""
    saa_s_product_summary: NotRequired[
        "aws_sdk_marketplace_catalog.types.saa_s_product_summary.SaaSProductSummary"
    ]
    """<p>An object that contains summary information about the SaaS product.</p>"""
    offer_summary: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_summary.OfferSummary"
    ]
    """<p>An object that contains summary information about the offer.</p>"""
    resale_authorization_summary: NotRequired[
        "aws_sdk_marketplace_catalog.types.resale_authorization_summary.ResaleAuthorizationSummary"
    ]
    """<p>An object that contains summary information about the Resale Authorization.</p>"""
    machine_learning_product_summary: NotRequired[
        "aws_sdk_marketplace_catalog.types.machine_learning_product_summary.MachineLearningProductSummary"
    ]
    offer_set_summary: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_set_summary.OfferSetSummary"
    ]
    """<p>An object that contains summary information about the offer set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntitySummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "entity_type" in value:
        out["EntityType"] = value["entity_type"]
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "entity_arn" in value:
        out["EntityArn"] = value["entity_arn"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "visibility" in value:
        out["Visibility"] = value["visibility"]
    if "ami_product_summary" in value:
        import aws_sdk_marketplace_catalog.types.ami_product_summary

        out["AmiProductSummary"] = (
            aws_sdk_marketplace_catalog.types.ami_product_summary.serialize_json(
                value["ami_product_summary"]
            )
        )
    if "container_product_summary" in value:
        import aws_sdk_marketplace_catalog.types.container_product_summary

        out["ContainerProductSummary"] = (
            aws_sdk_marketplace_catalog.types.container_product_summary.serialize_json(
                value["container_product_summary"]
            )
        )
    if "data_product_summary" in value:
        import aws_sdk_marketplace_catalog.types.data_product_summary

        out["DataProductSummary"] = (
            aws_sdk_marketplace_catalog.types.data_product_summary.serialize_json(
                value["data_product_summary"]
            )
        )
    if "saa_s_product_summary" in value:
        import aws_sdk_marketplace_catalog.types.saa_s_product_summary

        out["SaaSProductSummary"] = (
            aws_sdk_marketplace_catalog.types.saa_s_product_summary.serialize_json(
                value["saa_s_product_summary"]
            )
        )
    if "offer_summary" in value:
        import aws_sdk_marketplace_catalog.types.offer_summary

        out["OfferSummary"] = (
            aws_sdk_marketplace_catalog.types.offer_summary.serialize_json(
                value["offer_summary"]
            )
        )
    if "resale_authorization_summary" in value:
        import aws_sdk_marketplace_catalog.types.resale_authorization_summary

        out["ResaleAuthorizationSummary"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_summary.serialize_json(
                value["resale_authorization_summary"]
            )
        )
    if "machine_learning_product_summary" in value:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_summary

        out["MachineLearningProductSummary"] = (
            aws_sdk_marketplace_catalog.types.machine_learning_product_summary.serialize_json(
                value["machine_learning_product_summary"]
            )
        )
    if "offer_set_summary" in value:
        import aws_sdk_marketplace_catalog.types.offer_set_summary

        out["OfferSetSummary"] = (
            aws_sdk_marketplace_catalog.types.offer_set_summary.serialize_json(
                value["offer_set_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> EntitySummary:
    out: EntitySummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "EntityType" in data:
        out["entity_type"] = data["EntityType"]
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    if "EntityArn" in data:
        out["entity_arn"] = data["EntityArn"]
    if "LastModifiedDate" in data:
        out["last_modified_date"] = data["LastModifiedDate"]
    if "Visibility" in data:
        out["visibility"] = data["Visibility"]
    if "AmiProductSummary" in data:
        import aws_sdk_marketplace_catalog.types.ami_product_summary

        out["ami_product_summary"] = (
            aws_sdk_marketplace_catalog.types.ami_product_summary.deserialize_json(
                data["AmiProductSummary"]
            )
        )
    if "ContainerProductSummary" in data:
        import aws_sdk_marketplace_catalog.types.container_product_summary

        out["container_product_summary"] = (
            aws_sdk_marketplace_catalog.types.container_product_summary.deserialize_json(
                data["ContainerProductSummary"]
            )
        )
    if "DataProductSummary" in data:
        import aws_sdk_marketplace_catalog.types.data_product_summary

        out["data_product_summary"] = (
            aws_sdk_marketplace_catalog.types.data_product_summary.deserialize_json(
                data["DataProductSummary"]
            )
        )
    if "SaaSProductSummary" in data:
        import aws_sdk_marketplace_catalog.types.saa_s_product_summary

        out["saa_s_product_summary"] = (
            aws_sdk_marketplace_catalog.types.saa_s_product_summary.deserialize_json(
                data["SaaSProductSummary"]
            )
        )
    if "OfferSummary" in data:
        import aws_sdk_marketplace_catalog.types.offer_summary

        out["offer_summary"] = (
            aws_sdk_marketplace_catalog.types.offer_summary.deserialize_json(
                data["OfferSummary"]
            )
        )
    if "ResaleAuthorizationSummary" in data:
        import aws_sdk_marketplace_catalog.types.resale_authorization_summary

        out["resale_authorization_summary"] = (
            aws_sdk_marketplace_catalog.types.resale_authorization_summary.deserialize_json(
                data["ResaleAuthorizationSummary"]
            )
        )
    if "MachineLearningProductSummary" in data:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_summary

        out["machine_learning_product_summary"] = (
            aws_sdk_marketplace_catalog.types.machine_learning_product_summary.deserialize_json(
                data["MachineLearningProductSummary"]
            )
        )
    if "OfferSetSummary" in data:
        import aws_sdk_marketplace_catalog.types.offer_set_summary

        out["offer_set_summary"] = (
            aws_sdk_marketplace_catalog.types.offer_set_summary.deserialize_json(
                data["OfferSetSummary"]
            )
        )
    return out
