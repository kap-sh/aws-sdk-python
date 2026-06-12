"""Generated from Smithy shape ``com.amazonaws.ses#TemplateDoesNotExistException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ses.types.error_message
    import aws_sdk_ses.types.template_name


class TemplateDoesNotExistException_(TypedDict):
    template_name: NotRequired["aws_sdk_ses.types.template_name.TemplateName"]
    message: NotRequired["aws_sdk_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: TemplateDoesNotExistException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "template_name" in value:
        pairs.append((f"{prefix}.TemplateName", str(value["template_name"])))
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> TemplateDoesNotExistException_:
    out: TemplateDoesNotExistException_ = {}  # type: ignore[typeddict-item]
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TemplateDoesNotExistException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#TemplateDoesNotExistException``."""

    code: str | None = "TemplateDoesNotExistException"

    def __init__(self, data: TemplateDoesNotExistException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TemplateDoesNotExistException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "TemplateDoesNotExistException":
        return cls(deserialize_query(el))
