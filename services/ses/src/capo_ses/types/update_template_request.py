"""Generated from Smithy shape ``com.amazonaws.ses#UpdateTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.template


class UpdateTemplateRequest(TypedDict, closed=True):
    template: "capo_ses.types.template.Template"


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateTemplateRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.template

    capo_ses.types.template.serialize_query(
        value["template"], pairs, f"{prefix}.Template"
    )


def deserialize_query(el: Element) -> UpdateTemplateRequest:
    out: UpdateTemplateRequest = {}  # type: ignore[typeddict-item]
    child_template = el.find("Template")
    if child_template is not None:
        import capo_ses.types.template

        out["template"] = capo_ses.types.template.deserialize_query(child_template)
    else:
        raise DeserializationError("UpdateTemplateRequest.template required")
    return out
