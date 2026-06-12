"""Generated from Smithy shape ``com.amazonaws.guardduty#TrustedEntitySetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string

TrustedEntitySetIds: TypeAlias = list["aws_sdk_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: TrustedEntitySetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> TrustedEntitySetIds:
    return list(data)
