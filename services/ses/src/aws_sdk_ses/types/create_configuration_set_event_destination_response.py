"""Generated from Smithy shape ``com.amazonaws.ses#CreateConfigurationSetEventDestinationResponse``."""

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element


class CreateConfigurationSetEventDestinationResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateConfigurationSetEventDestinationResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> CreateConfigurationSetEventDestinationResponse:
    out: CreateConfigurationSetEventDestinationResponse = {}  # type: ignore[typeddict-item]
    return out
