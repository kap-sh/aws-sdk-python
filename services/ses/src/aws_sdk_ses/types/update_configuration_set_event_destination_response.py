"""Generated from Smithy shape ``com.amazonaws.ses#UpdateConfigurationSetEventDestinationResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class UpdateConfigurationSetEventDestinationResponse(TypedDict):
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
