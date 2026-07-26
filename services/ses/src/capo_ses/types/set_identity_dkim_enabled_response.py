"""Generated from Smithy shape ``com.amazonaws.ses#SetIdentityDkimEnabledResponse``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class SetIdentityDkimEnabledResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: SetIdentityDkimEnabledResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> SetIdentityDkimEnabledResponse:
    out: SetIdentityDkimEnabledResponse = {}  # type: ignore[typeddict-item]
    return out
