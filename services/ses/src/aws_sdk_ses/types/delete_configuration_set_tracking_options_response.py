"""Generated from Smithy shape ``com.amazonaws.ses#DeleteConfigurationSetTrackingOptionsResponse``."""

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element


class DeleteConfigurationSetTrackingOptionsResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteConfigurationSetTrackingOptionsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteConfigurationSetTrackingOptionsResponse:
    out: DeleteConfigurationSetTrackingOptionsResponse = {}  # type: ignore[typeddict-item]
    return out
