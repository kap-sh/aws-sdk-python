"""Generated from Smithy shape ``com.amazonaws.ses#PutConfigurationSetDeliveryOptionsResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class PutConfigurationSetDeliveryOptionsResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: PutConfigurationSetDeliveryOptionsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> PutConfigurationSetDeliveryOptionsResponse:
    out: PutConfigurationSetDeliveryOptionsResponse = {}  # type: ignore[typeddict-item]
    return out
