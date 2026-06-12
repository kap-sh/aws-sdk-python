"""Generated from Smithy shape ``com.amazonaws.ses#UpdateConfigurationSetTrackingOptionsResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class UpdateConfigurationSetTrackingOptionsResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateConfigurationSetTrackingOptionsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> UpdateConfigurationSetTrackingOptionsResponse:
    out: UpdateConfigurationSetTrackingOptionsResponse = {}  # type: ignore[typeddict-item]
    return out
