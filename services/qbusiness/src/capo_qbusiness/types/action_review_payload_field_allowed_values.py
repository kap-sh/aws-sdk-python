"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionReviewPayloadFieldAllowedValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.action_review_payload_field_allowed_value

ActionReviewPayloadFieldAllowedValues: TypeAlias = list[
    "capo_qbusiness.types.action_review_payload_field_allowed_value.ActionReviewPayloadFieldAllowedValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionReviewPayloadFieldAllowedValues) -> list:
    import capo_qbusiness.types.action_review_payload_field_allowed_value

    out: list = []
    for item in value:
        out.append(
            capo_qbusiness.types.action_review_payload_field_allowed_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ActionReviewPayloadFieldAllowedValues:
    import capo_qbusiness.types.action_review_payload_field_allowed_value

    out: ActionReviewPayloadFieldAllowedValues = []
    for item in data:
        out.append(
            capo_qbusiness.types.action_review_payload_field_allowed_value.deserialize_json(
                item
            )
        )
    return out
