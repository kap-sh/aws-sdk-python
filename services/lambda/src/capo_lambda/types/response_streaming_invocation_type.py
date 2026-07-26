"""Generated from Smithy shape ``com.amazonaws.lambda#ResponseStreamingInvocationType``."""

from typing import Literal, TypeAlias, cast

ResponseStreamingInvocationType: TypeAlias = Literal[
    "RequestResponse",
    "DryRun",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseStreamingInvocationType) -> str:
    return value


def deserialize_json(data: str) -> ResponseStreamingInvocationType:
    return cast(ResponseStreamingInvocationType, data)
