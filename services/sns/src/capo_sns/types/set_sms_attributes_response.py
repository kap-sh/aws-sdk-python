"""Generated from Smithy shape ``com.amazonaws.sns#SetSMSAttributesResponse``."""

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element


class SetSMSAttributesResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: SetSMSAttributesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> SetSMSAttributesResponse:
    out: SetSMSAttributesResponse = {}  # type: ignore[typeddict-item]
    return out
