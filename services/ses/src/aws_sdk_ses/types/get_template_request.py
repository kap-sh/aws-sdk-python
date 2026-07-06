"""Generated from Smithy shape ``com.amazonaws.ses#GetTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.template_name


class GetTemplateRequest(TypedDict, closed=True):
    template_name: "aws_sdk_ses.types.template_name.TemplateName"
    """<p>The name of the template to retrieve.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetTemplateRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.TemplateName", str(value["template_name"])))


def deserialize_query(el: Element) -> GetTemplateRequest:
    out: GetTemplateRequest = {}  # type: ignore[typeddict-item]
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    else:
        raise DeserializationError("GetTemplateRequest.template_name required")
    return out
