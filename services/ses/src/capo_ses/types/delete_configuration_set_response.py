"""Generated from Smithy shape ``com.amazonaws.ses#DeleteConfigurationSetResponse``."""

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element


class DeleteConfigurationSetResponse(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteConfigurationSetResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteConfigurationSetResponse:
    out: DeleteConfigurationSetResponse = {}  # type: ignore[typeddict-item]
    return out
