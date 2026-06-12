"""Generated from Smithy shape ``com.amazonaws.ses#DeleteTemplateResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class DeleteTemplateResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteTemplateResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteTemplateResponse:
    out: DeleteTemplateResponse = {}  # type: ignore[typeddict-item]
    return out
