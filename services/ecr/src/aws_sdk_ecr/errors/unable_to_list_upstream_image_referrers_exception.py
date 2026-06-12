"""Generated from Smithy shape ``com.amazonaws.ecr#UnableToListUpstreamImageReferrersException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message


class UnableToListUpstreamImageReferrersException_(TypedDict):
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnableToListUpstreamImageReferrersException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UnableToListUpstreamImageReferrersException_:
    out: UnableToListUpstreamImageReferrersException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnableToListUpstreamImageReferrersException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#UnableToListUpstreamImageReferrersException``."""

    code: str | None = "UnableToListUpstreamImageReferrersException"

    def __init__(self, data: UnableToListUpstreamImageReferrersException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnableToListUpstreamImageReferrersException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "UnableToListUpstreamImageReferrersException":
        return cls(deserialize_aws_json_1_1(data))
