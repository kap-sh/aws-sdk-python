"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionReviewPayload``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.action_payload_field_key
    import capo_qbusiness.types.action_review_payload_field

ActionReviewPayload: TypeAlias = dict[
    "capo_qbusiness.types.action_payload_field_key.ActionPayloadFieldKey",
    "capo_qbusiness.types.action_review_payload_field.ActionReviewPayloadField",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ActionReviewPayload) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_qbusiness.types.action_review_payload_field

        out[key] = capo_qbusiness.types.action_review_payload_field.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> ActionReviewPayload:
    out: ActionReviewPayload = {}
    for key, value in data.items():
        import capo_qbusiness.types.action_review_payload_field

        out[key] = capo_qbusiness.types.action_review_payload_field.deserialize_json(
            value
        )
    return out
