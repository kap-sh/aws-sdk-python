"""Generated from Smithy shape ``com.amazonaws.ses#CustomVerificationEmailTemplateAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ses.types.error_message
    import aws_sdk_ses.types.template_name


class CustomVerificationEmailTemplateAlreadyExistsException_(TypedDict, closed=True):
    custom_verification_email_template_name: NotRequired[
        "aws_sdk_ses.types.template_name.TemplateName"
    ]
    """<p>Indicates that the provided custom verification email template with the specified template name already exists.</p>"""
    message: NotRequired["aws_sdk_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomVerificationEmailTemplateAlreadyExistsException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "custom_verification_email_template_name" in value:
        pairs.append(
            (
                f"{prefix}.CustomVerificationEmailTemplateName",
                str(value["custom_verification_email_template_name"]),
            )
        )
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(
    el: Element,
) -> CustomVerificationEmailTemplateAlreadyExistsException_:
    out: CustomVerificationEmailTemplateAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    child_custom_verification_email_template_name = el.find(
        "CustomVerificationEmailTemplateName"
    )
    if child_custom_verification_email_template_name is not None:
        out["custom_verification_email_template_name"] = str(
            child_custom_verification_email_template_name.text or ""
        )
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CustomVerificationEmailTemplateAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#CustomVerificationEmailTemplateAlreadyExistsException``."""

    code: str | None = "CustomVerificationEmailTemplateAlreadyExistsException"

    def __init__(self, data: CustomVerificationEmailTemplateAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomVerificationEmailTemplateAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element
    ) -> "CustomVerificationEmailTemplateAlreadyExistsException":
        return cls(deserialize_query(el))
