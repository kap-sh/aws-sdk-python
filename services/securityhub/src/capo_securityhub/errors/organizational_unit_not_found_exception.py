"""Generated from Smithy shape ``com.amazonaws.securityhub#OrganizationalUnitNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityhub.errors import ServiceError

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class OrganizationalUnitNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    code: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalUnitNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_json(data: dict) -> OrganizationalUnitNotFoundException_:
    out: OrganizationalUnitNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    return out


class OrganizationalUnitNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.securityhub#OrganizationalUnitNotFoundException``."""

    code: str | None = "OrganizationalUnitNotFoundException"

    def __init__(self, data: OrganizationalUnitNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OrganizationalUnitNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "OrganizationalUnitNotFoundException":
        return cls(deserialize_json(data))
