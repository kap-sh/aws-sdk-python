"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RepositoryNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecr_public.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.exception_message


class RepositoryNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ecr_public.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryNotFoundException_:
    out: RepositoryNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class RepositoryNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecrpublic#RepositoryNotFoundException``."""

    code: str | None = "RepositoryNotFoundException"

    def __init__(self, data: RepositoryNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RepositoryNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "RepositoryNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
