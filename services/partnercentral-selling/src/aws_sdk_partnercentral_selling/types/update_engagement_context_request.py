"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#UpdateEngagementContextRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.date_time
    import aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier
    import aws_sdk_partnercentral_selling.types.engagement_context_identifier
    import aws_sdk_partnercentral_selling.types.engagement_context_type
    import aws_sdk_partnercentral_selling.types.update_engagement_context_payload


class UpdateEngagementContextRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the engagement context update request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the engagement context is updated in.</p>"""
    engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_arn_or_identifier.EngagementArnOrIdentifier"
    """<p>The unique identifier of the <code>Engagement</code> containing the context to be updated. This parameter ensures the context update is applied to the correct engagement.</p>"""
    context_identifier: "aws_sdk_partnercentral_selling.types.engagement_context_identifier.EngagementContextIdentifier"
    """<p>The unique identifier of the specific engagement context to be updated. This ensures that the correct context within the engagement is modified.</p>"""
    engagement_last_modified_at: (
        "aws_sdk_partnercentral_selling.types.date_time.DateTime"
    )
    """<p>The timestamp when the engagement was last modified, used for optimistic concurrency control. This helps prevent conflicts when multiple users attempt to update the same engagement simultaneously.</p>"""
    type: "aws_sdk_partnercentral_selling.types.engagement_context_type.EngagementContextType"
    """<p>Specifies the type of context being updated within the engagement. This field determines the structure and content of the context payload being modified.</p>"""
    payload: "aws_sdk_partnercentral_selling.types.update_engagement_context_payload.UpdateEngagementContextPayload"
    """<p>Contains the updated contextual information for the engagement. The structure of this payload varies based on the context type specified in the Type field.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEngagementContextRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["EngagementIdentifier"] = value["engagement_identifier"]
    out["ContextIdentifier"] = value["context_identifier"]
    import aws_sdk_partnercentral_selling.types.date_time

    out["EngagementLastModifiedAt"] = (
        aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
            value["engagement_last_modified_at"]
        )
    )
    import aws_sdk_partnercentral_selling.types.engagement_context_type

    out["Type"] = (
        aws_sdk_partnercentral_selling.types.engagement_context_type.serialize_aws_json_1_0(
            value["type"]
        )
    )
    import aws_sdk_partnercentral_selling.types.update_engagement_context_payload

    out["Payload"] = (
        aws_sdk_partnercentral_selling.types.update_engagement_context_payload.serialize_aws_json_1_0(
            value["payload"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEngagementContextRequest:
    out: UpdateEngagementContextRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("UpdateEngagementContextRequest.catalog required")
    if "EngagementIdentifier" in data:
        out["engagement_identifier"] = data["EngagementIdentifier"]
    else:
        raise DeserializationError(
            "UpdateEngagementContextRequest.engagement_identifier required"
        )
    if "ContextIdentifier" in data:
        out["context_identifier"] = data["ContextIdentifier"]
    else:
        raise DeserializationError(
            "UpdateEngagementContextRequest.context_identifier required"
        )
    if "EngagementLastModifiedAt" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["engagement_last_modified_at"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["EngagementLastModifiedAt"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateEngagementContextRequest.engagement_last_modified_at required"
        )
    if "Type" in data:
        import aws_sdk_partnercentral_selling.types.engagement_context_type

        out["type"] = (
            aws_sdk_partnercentral_selling.types.engagement_context_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("UpdateEngagementContextRequest.type required")
    if "Payload" in data:
        import aws_sdk_partnercentral_selling.types.update_engagement_context_payload

        out["payload"] = (
            aws_sdk_partnercentral_selling.types.update_engagement_context_payload.deserialize_aws_json_1_0(
                data["Payload"]
            )
        )
    else:
        raise DeserializationError("UpdateEngagementContextRequest.payload required")
    return out
