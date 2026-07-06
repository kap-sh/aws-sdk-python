"""Generated from Smithy shape ``com.amazonaws.securitylake#ResourceNotFoundException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_securitylake.errors import ServiceError


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["str"]
    resource_name: NotRequired["str"]
    """<p>The name of the resource that could not be found.</p>"""
    resource_type: NotRequired["str"]
    """<p>The type of the resource that could not be found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.securitylake#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_json(data))
