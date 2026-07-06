"""Generated from Smithy shape ``com.amazonaws.securitylake#SqsNotificationConfiguration``."""

from typing_extensions import TypedDict


class SqsNotificationConfiguration(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: SqsNotificationConfiguration) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SqsNotificationConfiguration:
    out: SqsNotificationConfiguration = {}  # type: ignore[typeddict-item]
    return out
