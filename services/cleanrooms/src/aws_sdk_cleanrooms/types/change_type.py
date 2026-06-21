"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeType``."""

from typing import Literal, TypeAlias, cast

ChangeType: TypeAlias = Literal[
    "ADD_MEMBER",
    "GRANT_RECEIVE_RESULTS_ABILITY",
    "REVOKE_RECEIVE_RESULTS_ABILITY",
    "EDIT_AUTO_APPROVED_CHANGE_TYPES",
    "ADD_PAYER_CANDIDATE",
    "REMOVE_PAYER_CANDIDATE",
    "GRANT_CAN_RECEIVE_MODEL_OUTPUT",
    "GRANT_CAN_RECEIVE_INFERENCE_OUTPUT",
    "REVOKE_CAN_RECEIVE_MODEL_OUTPUT",
    "REVOKE_CAN_RECEIVE_INFERENCE_OUTPUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeType) -> str:
    return value


def deserialize_json(data: str) -> ChangeType:
    return cast(ChangeType, data)
