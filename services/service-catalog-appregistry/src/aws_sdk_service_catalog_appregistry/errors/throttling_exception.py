"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ThrottlingException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog_appregistry.errors import (
    DeserializationError,
    ServiceError,
)

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.string


class ThrottlingException_(TypedDict):
    message: "aws_sdk_service_catalog_appregistry.types.string.String"
    """<p>A message associated with the Throttling exception.</p>"""
    service_code: NotRequired["aws_sdk_service_catalog_appregistry.types.string.String"]
    """<p>The originating service code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicecatalogappregistry#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))
