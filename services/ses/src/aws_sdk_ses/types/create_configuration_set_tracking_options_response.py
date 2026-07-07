"""Generated from Smithy shape ``com.amazonaws.ses#CreateConfigurationSetTrackingOptionsResponse``."""

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element


class CreateConfigurationSetTrackingOptionsResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateConfigurationSetTrackingOptionsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> CreateConfigurationSetTrackingOptionsResponse:
    out: CreateConfigurationSetTrackingOptionsResponse = {}  # type: ignore[typeddict-item]
    return out
