"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionRequestSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.decision_comment
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.metadata_forms_summary
    import aws_sdk_datazone.types.request_reason
    import aws_sdk_datazone.types.subscribed_listings
    import aws_sdk_datazone.types.subscribed_principals
    import aws_sdk_datazone.types.subscription_id
    import aws_sdk_datazone.types.subscription_request_id
    import aws_sdk_datazone.types.subscription_request_status
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class SubscriptionRequestSummary(TypedDict):
    id: "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId"
    """<p>The identifier of the subscription request.</p>"""
    created_by: "aws_sdk_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the subscription request.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The identifier of the Amazon DataZone user who updated the subscription request.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a subscription request exists.</p>"""
    status: (
        "aws_sdk_datazone.types.subscription_request_status.SubscriptionRequestStatus"
    )
    """<p>The status of the subscription request.</p>"""
    created_at: "aws_sdk_datazone.types.created_at.CreatedAt"
    """<p>The timestamp of when a subscription request was created.</p>"""
    updated_at: "aws_sdk_datazone.types.updated_at.UpdatedAt"
    """<p>The timestamp of when the subscription request was updated.</p>"""
    request_reason: "aws_sdk_datazone.types.request_reason.RequestReason"
    """<p>The reason for the subscription request.</p>"""
    subscribed_principals: (
        "aws_sdk_datazone.types.subscribed_principals.SubscribedPrincipals"
    )
    """<p>The principals included in the subscription request. </p>"""
    subscribed_listings: "aws_sdk_datazone.types.subscribed_listings.SubscribedListings"
    """<p>The listings included in the subscription request.</p>"""
    reviewer_id: NotRequired["str"]
    """<p>The identifier of the subscription request reviewer.</p>"""
    decision_comment: NotRequired[
        "aws_sdk_datazone.types.decision_comment.DecisionComment"
    ]
    """<p>The decision comment of the subscription request.</p>"""
    existing_subscription_id: NotRequired[
        "aws_sdk_datazone.types.subscription_id.SubscriptionId"
    ]
    """<p>The ID of the existing subscription.</p>"""
    metadata_forms_summary: NotRequired[
        "aws_sdk_datazone.types.metadata_forms_summary.MetadataFormsSummary"
    ]
    """<p>The summary of the metadata forms.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionRequestSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["createdBy"] = value["created_by"]
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["domainId"] = value["domain_id"]
    import aws_sdk_datazone.types.subscription_request_status

    out["status"] = aws_sdk_datazone.types.subscription_request_status.serialize_json(
        value["status"]
    )
    import aws_sdk_datazone.types.created_at

    out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    import aws_sdk_datazone.types.updated_at

    out["updatedAt"] = aws_sdk_datazone.types.updated_at.serialize_json(
        value["updated_at"]
    )
    out["requestReason"] = value["request_reason"]
    import aws_sdk_datazone.types.subscribed_principals

    out["subscribedPrincipals"] = (
        aws_sdk_datazone.types.subscribed_principals.serialize_json(
            value["subscribed_principals"]
        )
    )
    import aws_sdk_datazone.types.subscribed_listings

    out["subscribedListings"] = (
        aws_sdk_datazone.types.subscribed_listings.serialize_json(
            value["subscribed_listings"]
        )
    )
    if "reviewer_id" in value:
        out["reviewerId"] = value["reviewer_id"]
    if "decision_comment" in value:
        out["decisionComment"] = value["decision_comment"]
    if "existing_subscription_id" in value:
        out["existingSubscriptionId"] = value["existing_subscription_id"]
    if "metadata_forms_summary" in value:
        import aws_sdk_datazone.types.metadata_forms_summary

        out["metadataFormsSummary"] = (
            aws_sdk_datazone.types.metadata_forms_summary.serialize_json(
                value["metadata_forms_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubscriptionRequestSummary:
    out: SubscriptionRequestSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("SubscriptionRequestSummary.id required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("SubscriptionRequestSummary.created_by required")
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("SubscriptionRequestSummary.domain_id required")
    if "status" in data:
        import aws_sdk_datazone.types.subscription_request_status

        out["status"] = (
            aws_sdk_datazone.types.subscription_request_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("SubscriptionRequestSummary.status required")
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("SubscriptionRequestSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("SubscriptionRequestSummary.updated_at required")
    if "requestReason" in data:
        out["request_reason"] = data["requestReason"]
    else:
        raise DeserializationError("SubscriptionRequestSummary.request_reason required")
    if "subscribedPrincipals" in data:
        import aws_sdk_datazone.types.subscribed_principals

        out["subscribed_principals"] = (
            aws_sdk_datazone.types.subscribed_principals.deserialize_json(
                data["subscribedPrincipals"]
            )
        )
    else:
        raise DeserializationError(
            "SubscriptionRequestSummary.subscribed_principals required"
        )
    if "subscribedListings" in data:
        import aws_sdk_datazone.types.subscribed_listings

        out["subscribed_listings"] = (
            aws_sdk_datazone.types.subscribed_listings.deserialize_json(
                data["subscribedListings"]
            )
        )
    else:
        raise DeserializationError(
            "SubscriptionRequestSummary.subscribed_listings required"
        )
    if "reviewerId" in data:
        out["reviewer_id"] = data["reviewerId"]
    if "decisionComment" in data:
        out["decision_comment"] = data["decisionComment"]
    if "existingSubscriptionId" in data:
        out["existing_subscription_id"] = data["existingSubscriptionId"]
    if "metadataFormsSummary" in data:
        import aws_sdk_datazone.types.metadata_forms_summary

        out["metadata_forms_summary"] = (
            aws_sdk_datazone.types.metadata_forms_summary.deserialize_json(
                data["metadataFormsSummary"]
            )
        )
    return out
