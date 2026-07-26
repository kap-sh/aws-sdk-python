"""Generated from Smithy shape ``com.amazonaws.polly#ThrottlingReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_polly.types.throttling_reason

ThrottlingReasonList: TypeAlias = list[
    "capo_polly.types.throttling_reason.ThrottlingReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingReasonList) -> list:
    import capo_polly.types.throttling_reason

    out: list = []
    for item in value:
        out.append(capo_polly.types.throttling_reason.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThrottlingReasonList:
    import capo_polly.types.throttling_reason

    out: ThrottlingReasonList = []
    for item in data:
        out.append(capo_polly.types.throttling_reason.deserialize_json(item))
    return out
