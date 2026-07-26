"""Generated from Smithy shape ``com.amazonaws.ses#PutConfigurationSetDeliveryOptionsResponse``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class PutConfigurationSetDeliveryOptionsResponse(TypedDict, closed=True):
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
