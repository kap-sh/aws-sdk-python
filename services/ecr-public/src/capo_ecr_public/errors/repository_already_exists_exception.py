"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RepositoryAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr_public.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecr_public.types.exception_message


class RepositoryAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_ecr_public.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryAlreadyExistsException_:
    out: RepositoryAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class RepositoryAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecrpublic#RepositoryAlreadyExistsException``."""

    code: str | None = "RepositoryAlreadyExistsException"

    def __init__(self, data: RepositoryAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RepositoryAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "RepositoryAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
