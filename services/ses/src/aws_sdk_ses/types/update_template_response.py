"""Generated from Smithy shape ``com.amazonaws.ses#UpdateTemplateResponse``."""

from typing import TypedDict

from aws_sdk_ses._protocol.xml import Element


class UpdateTemplateResponse(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateTemplateResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> UpdateTemplateResponse:
    out: UpdateTemplateResponse = {}  # type: ignore[typeddict-item]
    return out
