"""Generated from Smithy shape ``com.amazonaws.ses#GetTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.template


class GetTemplateResponse(TypedDict, closed=True):
    template: NotRequired["capo_ses.types.template.Template"]


# --- awsQuery ser/de ---
def serialize_query(
    value: GetTemplateResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "template" in value:
        import capo_ses.types.template

        capo_ses.types.template.serialize_query(
            value["template"], pairs, f"{key_prefix}Template"
        )


def deserialize_query(el: Element) -> GetTemplateResponse:
    out: GetTemplateResponse = {}  # type: ignore[typeddict-item]
    child_template = el.find("Template")
    if child_template is not None:
        import capo_ses.types.template

        out["template"] = capo_ses.types.template.deserialize_query(child_template)
    return out
