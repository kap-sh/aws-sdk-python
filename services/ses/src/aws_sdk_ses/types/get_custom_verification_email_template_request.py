"""Generated from Smithy shape ``com.amazonaws.ses#GetCustomVerificationEmailTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.template_name


class GetCustomVerificationEmailTemplateRequest(TypedDict):
    template_name: "aws_sdk_ses.types.template_name.TemplateName"
    """<p>The name of the custom verification email template to retrieve.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetCustomVerificationEmailTemplateRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.TemplateName", str(value["template_name"])))


def deserialize_query(el: Element) -> GetCustomVerificationEmailTemplateRequest:
    out: GetCustomVerificationEmailTemplateRequest = {}  # type: ignore[typeddict-item]
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    else:
        raise DeserializationError(
            "GetCustomVerificationEmailTemplateRequest.template_name required"
        )
    return out
