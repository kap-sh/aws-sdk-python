"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionReviewPayload``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_payload_field_key
    import aws_sdk_qbusiness.types.action_review_payload_field

ActionReviewPayload: TypeAlias = dict[
    "aws_sdk_qbusiness.types.action_payload_field_key.ActionPayloadFieldKey",
    "aws_sdk_qbusiness.types.action_review_payload_field.ActionReviewPayloadField",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ActionReviewPayload) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_qbusiness.types.action_review_payload_field

        out[key] = aws_sdk_qbusiness.types.action_review_payload_field.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> ActionReviewPayload:
    out: ActionReviewPayload = {}
    for key, value in data.items():
        import aws_sdk_qbusiness.types.action_review_payload_field

        out[key] = aws_sdk_qbusiness.types.action_review_payload_field.deserialize_json(
            value
        )
    return out
