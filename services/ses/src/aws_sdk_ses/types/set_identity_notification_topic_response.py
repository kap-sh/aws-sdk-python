"""Generated from Smithy shape ``com.amazonaws.ses#SetIdentityNotificationTopicResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class SetIdentityNotificationTopicResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: SetIdentityNotificationTopicResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> SetIdentityNotificationTopicResponse:
    out: SetIdentityNotificationTopicResponse = {}  # type: ignore[typeddict-item]
    return out
