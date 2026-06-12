"""Generated from Smithy shape ``com.amazonaws.sesv2#ReputationEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.amazon_resource_name
    import aws_sdk_sesv2.types.recommendation_impact
    import aws_sdk_sesv2.types.reputation_entity_reference
    import aws_sdk_sesv2.types.reputation_entity_type
    import aws_sdk_sesv2.types.sending_status
    import aws_sdk_sesv2.types.status_record


class ReputationEntity(TypedDict):
    reputation_entity_reference: NotRequired[
        "aws_sdk_sesv2.types.reputation_entity_reference.ReputationEntityReference"
    ]
    """<p>The unique identifier for the reputation entity. For resource-type entities, this is the Amazon Resource Name (ARN) of the resource.</p>"""
    reputation_entity_type: NotRequired[
        "aws_sdk_sesv2.types.reputation_entity_type.ReputationEntityType"
    ]
    """<p>The type of reputation entity. Currently, only <code>RESOURCE</code> type entities are supported.</p>"""
    reputation_management_policy: NotRequired[
        "aws_sdk_sesv2.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the reputation management policy applied to this entity. This is an Amazon Web Services Amazon SES-managed policy.</p>"""
    customer_managed_status: NotRequired[
        "aws_sdk_sesv2.types.status_record.StatusRecord"
    ]
    """<p>The customer-managed status record for this reputation entity, including the current status, cause description, and last updated timestamp.</p>"""
    aws_ses_managed_status: NotRequired[
        "aws_sdk_sesv2.types.status_record.StatusRecord"
    ]
    """<p>The Amazon Web Services Amazon SES-managed status record for this reputation entity, including the current status, cause description, and last updated timestamp.</p>"""
    sending_status_aggregate: NotRequired[
        "aws_sdk_sesv2.types.sending_status.SendingStatus"
    ]
    """<p>The aggregate sending status that determines whether the entity is allowed to send emails. This status is derived from both the customer-managed and Amazon Web Services Amazon SES-managed statuses. If either the customer-managed status or the Amazon Web Services Amazon SES-managed status is <code>DISABLED</code>, the aggregate status will be <code>DISABLED</code> and the entity will not be allowed to send emails. When the customer-managed status is set to <code>REINSTATED</code>, the entity can continue sending even if there are active reputation findings, provided the Amazon Web Services Amazon SES-managed status also permits sending. The entity can only send emails when both statuses permit sending.</p>"""
    reputation_impact: NotRequired[
        "aws_sdk_sesv2.types.recommendation_impact.RecommendationImpact"
    ]
    """<p>The reputation impact level for this entity, representing the highest impact reputation finding currently active. Reputation findings can be retrieved using the <code>ListRecommendations</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReputationEntity) -> dict:
    out: dict = {}
    if "reputation_entity_reference" in value:
        out["ReputationEntityReference"] = value["reputation_entity_reference"]
    if "reputation_entity_type" in value:
        import aws_sdk_sesv2.types.reputation_entity_type

        out["ReputationEntityType"] = (
            aws_sdk_sesv2.types.reputation_entity_type.serialize_json(
                value["reputation_entity_type"]
            )
        )
    if "reputation_management_policy" in value:
        out["ReputationManagementPolicy"] = value["reputation_management_policy"]
    if "customer_managed_status" in value:
        import aws_sdk_sesv2.types.status_record

        out["CustomerManagedStatus"] = aws_sdk_sesv2.types.status_record.serialize_json(
            value["customer_managed_status"]
        )
    if "aws_ses_managed_status" in value:
        import aws_sdk_sesv2.types.status_record

        out["AwsSesManagedStatus"] = aws_sdk_sesv2.types.status_record.serialize_json(
            value["aws_ses_managed_status"]
        )
    if "sending_status_aggregate" in value:
        import aws_sdk_sesv2.types.sending_status

        out["SendingStatusAggregate"] = (
            aws_sdk_sesv2.types.sending_status.serialize_json(
                value["sending_status_aggregate"]
            )
        )
    if "reputation_impact" in value:
        import aws_sdk_sesv2.types.recommendation_impact

        out["ReputationImpact"] = (
            aws_sdk_sesv2.types.recommendation_impact.serialize_json(
                value["reputation_impact"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReputationEntity:
    out: ReputationEntity = {}  # type: ignore[typeddict-item]
    if "ReputationEntityReference" in data:
        out["reputation_entity_reference"] = data["ReputationEntityReference"]
    if "ReputationEntityType" in data:
        import aws_sdk_sesv2.types.reputation_entity_type

        out["reputation_entity_type"] = (
            aws_sdk_sesv2.types.reputation_entity_type.deserialize_json(
                data["ReputationEntityType"]
            )
        )
    if "ReputationManagementPolicy" in data:
        out["reputation_management_policy"] = data["ReputationManagementPolicy"]
    if "CustomerManagedStatus" in data:
        import aws_sdk_sesv2.types.status_record

        out["customer_managed_status"] = (
            aws_sdk_sesv2.types.status_record.deserialize_json(
                data["CustomerManagedStatus"]
            )
        )
    if "AwsSesManagedStatus" in data:
        import aws_sdk_sesv2.types.status_record

        out["aws_ses_managed_status"] = (
            aws_sdk_sesv2.types.status_record.deserialize_json(
                data["AwsSesManagedStatus"]
            )
        )
    if "SendingStatusAggregate" in data:
        import aws_sdk_sesv2.types.sending_status

        out["sending_status_aggregate"] = (
            aws_sdk_sesv2.types.sending_status.deserialize_json(
                data["SendingStatusAggregate"]
            )
        )
    if "ReputationImpact" in data:
        import aws_sdk_sesv2.types.recommendation_impact

        out["reputation_impact"] = (
            aws_sdk_sesv2.types.recommendation_impact.deserialize_json(
                data["ReputationImpact"]
            )
        )
    return out
