"""Generated from Smithy shape ``com.amazonaws.sesv2#UpdateReputationEntityPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.amazon_resource_name
    import aws_sdk_sesv2.types.reputation_entity_reference
    import aws_sdk_sesv2.types.reputation_entity_type


class UpdateReputationEntityPolicyRequest(TypedDict):
    reputation_entity_type: (
        "aws_sdk_sesv2.types.reputation_entity_type.ReputationEntityType"
    )
    """<p>The type of reputation entity. Currently, only <code>RESOURCE</code> type entities are supported.</p>"""
    reputation_entity_reference: (
        "aws_sdk_sesv2.types.reputation_entity_reference.ReputationEntityReference"
    )
    """<p>The unique identifier for the reputation entity. For resource-type entities, this is the Amazon Resource Name (ARN) of the resource.</p>"""
    reputation_entity_policy: (
        "aws_sdk_sesv2.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the reputation management policy to apply to this entity. This is an Amazon Web Services Amazon SES-managed policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReputationEntityPolicyRequest) -> dict:
    out: dict = {}
    out["ReputationEntityPolicy"] = value["reputation_entity_policy"]
    return out


def deserialize_json(data: dict) -> UpdateReputationEntityPolicyRequest:
    out: UpdateReputationEntityPolicyRequest = {}  # type: ignore[typeddict-item]
    if "ReputationEntityPolicy" in data:
        out["reputation_entity_policy"] = data["ReputationEntityPolicy"]
    else:
        raise DeserializationError(
            "UpdateReputationEntityPolicyRequest.reputation_entity_policy required"
        )
    return out
