"""Generated from Smithy shape ``com.amazonaws.marketplacedeployment#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_marketplace_deployment.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_marketplace_deployment.types.resource_id


class ConflictException_(TypedDict, closed=True):
    message: "str"
    resource_id: "capo_marketplace_deployment.types.resource_id.ResourceId"
    """<p>The unique identifier for the resource associated with the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ConflictException_.resource_id required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacedeployment#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))
