"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteSubscriptionTargetInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.subscription_target_id


class DeleteSubscriptionTargetInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription target is deleted.</p>"""
    environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the Amazon DataZone environment in which the subscription target is deleted.</p>"""
    identifier: "aws_sdk_datazone.types.subscription_target_id.SubscriptionTargetId"
    """<p>The ID of the subscription target that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSubscriptionTargetInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSubscriptionTargetInput:
    out: DeleteSubscriptionTargetInput = {}  # type: ignore[typeddict-item]
    return out
