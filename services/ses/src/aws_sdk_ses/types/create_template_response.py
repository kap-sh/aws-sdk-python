"""Generated from Smithy shape ``com.amazonaws.ses#CreateTemplateResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class CreateTemplateResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateTemplateResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> CreateTemplateResponse:
    out: CreateTemplateResponse = {}  # type: ignore[typeddict-item]
    return out
