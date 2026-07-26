"""Generated from Smithy shape ``com.amazonaws.ses#UpdateConfigurationSetEventDestinationResponse``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class UpdateConfigurationSetEventDestinationResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateConfigurationSetEventDestinationResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> UpdateConfigurationSetEventDestinationResponse:
    out: UpdateConfigurationSetEventDestinationResponse = {}  # type: ignore[typeddict-item]
    return out
