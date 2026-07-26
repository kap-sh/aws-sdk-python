"""Generated from Smithy shape ``com.amazonaws.ses#DeleteIdentityResponse``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class DeleteIdentityResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteIdentityResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteIdentityResponse:
    out: DeleteIdentityResponse = {}  # type: ignore[typeddict-item]
    return out
