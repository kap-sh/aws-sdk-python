"""Generated from Smithy shape ``com.amazonaws.ses#SetIdentityFeedbackForwardingEnabledResponse``."""

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element


class SetIdentityFeedbackForwardingEnabledResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: SetIdentityFeedbackForwardingEnabledResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> SetIdentityFeedbackForwardingEnabledResponse:
    out: SetIdentityFeedbackForwardingEnabledResponse = {}  # type: ignore[typeddict-item]
    return out
