"""Generated from Smithy shape ``com.amazonaws.ses#GetTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.template


class GetTemplateResponse(TypedDict):
    template: NotRequired["aws_sdk_ses.types.template.Template"]


# --- awsQuery ser/de ---
def serialize_query(
    value: GetTemplateResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "template" in value:
        import aws_sdk_ses.types.template

        aws_sdk_ses.types.template.serialize_query(
            value["template"], pairs, f"{prefix}.Template"
        )


def deserialize_query(el: Element) -> GetTemplateResponse:
    out: GetTemplateResponse = {}  # type: ignore[typeddict-item]
    child_template = el.find("Template")
    if child_template is not None:
        import aws_sdk_ses.types.template

        out["template"] = aws_sdk_ses.types.template.deserialize_query(child_template)
    return out
