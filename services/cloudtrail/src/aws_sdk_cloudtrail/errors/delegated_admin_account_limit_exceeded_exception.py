"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DelegatedAdminAccountLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.error_message


class DelegatedAdminAccountLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DelegatedAdminAccountLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DelegatedAdminAccountLimitExceededException_:
    out: DelegatedAdminAccountLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DelegatedAdminAccountLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#DelegatedAdminAccountLimitExceededException``."""

    code: str | None = "DelegatedAdminAccountLimitExceededException"

    def __init__(self, data: DelegatedAdminAccountLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DelegatedAdminAccountLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "DelegatedAdminAccountLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
