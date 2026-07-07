"""Generated from Smithy shape ``com.amazonaws.ses#CreateTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.template


class CreateTemplateRequest(TypedDict, closed=True):
    template: "aws_sdk_ses.types.template.Template"
    """<p>The content of the email, composed of a subject line and either an HTML part or a text-only part.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateTemplateRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.template

    aws_sdk_ses.types.template.serialize_query(
        value["template"], pairs, f"{prefix}.Template"
    )


def deserialize_query(el: Element) -> CreateTemplateRequest:
    out: CreateTemplateRequest = {}  # type: ignore[typeddict-item]
    child_template = el.find("Template")
    if child_template is not None:
        import aws_sdk_ses.types.template

        out["template"] = aws_sdk_ses.types.template.deserialize_query(child_template)
    else:
        raise DeserializationError("CreateTemplateRequest.template required")
    return out
