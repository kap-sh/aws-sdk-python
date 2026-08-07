"""Generated from Smithy shape ``com.amazonaws.ses#TestRenderTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.rendered_template


class TestRenderTemplateResponse(TypedDict, closed=True):
    rendered_template: NotRequired["capo_ses.types.rendered_template.RenderedTemplate"]
    """<p>The complete MIME message rendered by applying the data in the TemplateData parameter to the template specified in the TemplateName parameter.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TestRenderTemplateResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rendered_template" in value:
        pairs.append((f"{key_prefix}RenderedTemplate", str(value["rendered_template"])))


def deserialize_query(el: Element) -> TestRenderTemplateResponse:
    out: TestRenderTemplateResponse = {}  # type: ignore[typeddict-item]
    child_rendered_template = el.find("RenderedTemplate")
    if child_rendered_template is not None:
        out["rendered_template"] = str(child_rendered_template.text or "")
    return out
