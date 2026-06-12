"""Generated from Smithy shape ``com.amazonaws.securityhub#OrganizationNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_securityhub.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class OrganizationNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    code: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_json(data: dict) -> OrganizationNotFoundException_:
    out: OrganizationNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    return out


class OrganizationNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.securityhub#OrganizationNotFoundException``."""

    code: str | None = "OrganizationNotFoundException"

    def __init__(self, data: OrganizationNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OrganizationNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "OrganizationNotFoundException":
        return cls(deserialize_json(data))
