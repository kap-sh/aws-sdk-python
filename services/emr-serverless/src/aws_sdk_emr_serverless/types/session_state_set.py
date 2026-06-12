"""Generated from Smithy shape ``com.amazonaws.emrserverless#SessionStateSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.session_state

SessionStateSet: TypeAlias = list[
    "aws_sdk_emr_serverless.types.session_state.SessionState"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionStateSet) -> list:
    return list(value)


def deserialize_json(data: list) -> SessionStateSet:
    return list(data)
