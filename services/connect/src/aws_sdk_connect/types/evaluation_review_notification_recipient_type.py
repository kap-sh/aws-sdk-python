"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationReviewNotificationRecipientType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationReviewNotificationRecipientType: TypeAlias = Literal["USER_ID",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("USER_ID",))


def serialize_json(value: EvaluationReviewNotificationRecipientType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationReviewNotificationRecipientType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationReviewNotificationRecipientType value: {data!r}"
        )
    return cast(EvaluationReviewNotificationRecipientType, data)
