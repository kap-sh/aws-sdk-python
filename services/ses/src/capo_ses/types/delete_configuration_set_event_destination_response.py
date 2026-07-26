"""Generated from Smithy shape ``com.amazonaws.ses#DeleteConfigurationSetEventDestinationResponse``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class DeleteConfigurationSetEventDestinationResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteConfigurationSetEventDestinationResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteConfigurationSetEventDestinationResponse:
    out: DeleteConfigurationSetEventDestinationResponse = {}  # type: ignore[typeddict-item]
    return out
