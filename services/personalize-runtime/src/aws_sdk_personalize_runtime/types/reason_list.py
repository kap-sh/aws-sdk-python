"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#ReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.reason

ReasonList: TypeAlias = list["aws_sdk_personalize_runtime.types.reason.Reason"]


# --- restJson1 ser/de ---
def serialize_json(value: ReasonList) -> list:
    return list(value)


def deserialize_json(data: list) -> ReasonList:
    return list(data)
