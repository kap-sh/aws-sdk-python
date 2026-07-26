"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionExecutionPayload``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.action_execution_payload_field
    import capo_qbusiness.types.action_payload_field_key

ActionExecutionPayload: TypeAlias = dict[
    "capo_qbusiness.types.action_payload_field_key.ActionPayloadFieldKey",
    "capo_qbusiness.types.action_execution_payload_field.ActionExecutionPayloadField",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ActionExecutionPayload) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_qbusiness.types.action_execution_payload_field

        out[key] = capo_qbusiness.types.action_execution_payload_field.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> ActionExecutionPayload:
    out: ActionExecutionPayload = {}
    for key, value in data.items():
        import capo_qbusiness.types.action_execution_payload_field

        out[key] = capo_qbusiness.types.action_execution_payload_field.deserialize_json(
            value
        )
    return out
