"""Generated from Smithy shape ``com.amazonaws.codecommit#MaximumRuleTemplatesAssociatedWithRepositoryException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.message


class MaximumRuleTemplatesAssociatedWithRepositoryException_(TypedDict):
    message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: MaximumRuleTemplatesAssociatedWithRepositoryException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> MaximumRuleTemplatesAssociatedWithRepositoryException_:
    out: MaximumRuleTemplatesAssociatedWithRepositoryException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MaximumRuleTemplatesAssociatedWithRepositoryException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#MaximumRuleTemplatesAssociatedWithRepositoryException``."""

    code: str | None = "MaximumRuleTemplatesAssociatedWithRepositoryException"

    def __init__(self, data: MaximumRuleTemplatesAssociatedWithRepositoryException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MaximumRuleTemplatesAssociatedWithRepositoryException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "MaximumRuleTemplatesAssociatedWithRepositoryException":
        return cls(deserialize_aws_json_1_1(data))
