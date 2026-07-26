"""Generated from Smithy shape ``com.amazonaws.ses#UpdateConfigurationSetTrackingOptionsResponse``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class UpdateConfigurationSetTrackingOptionsResponse(TypedDict, closed=True):
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
