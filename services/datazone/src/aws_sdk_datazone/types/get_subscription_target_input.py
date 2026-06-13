"""Generated from Smithy shape ``com.amazonaws.datazone#GetSubscriptionTargetInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.subscription_target_id


class GetSubscriptionTargetInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription target exists.</p>"""
    environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the environment associated with the subscription target.</p>"""
    identifier: "aws_sdk_datazone.types.subscription_target_id.SubscriptionTargetId"
    """<p>The ID of the subscription target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionTargetInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSubscriptionTargetInput:
    out: GetSubscriptionTargetInput = {}  # type: ignore[typeddict-item]
    return out
