"""Generated from Smithy shape ``com.amazonaws.ses#CreateConfigurationSetResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class CreateConfigurationSetResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateConfigurationSetResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> CreateConfigurationSetResponse:
    out: CreateConfigurationSetResponse = {}  # type: ignore[typeddict-item]
    return out
