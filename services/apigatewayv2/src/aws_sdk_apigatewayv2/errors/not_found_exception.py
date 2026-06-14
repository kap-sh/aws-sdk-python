"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#NotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_apigatewayv2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class NotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>Describes the error encountered.</p>"""
    resource_type: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> NotFoundException_:
    out: NotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out


class NotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.apigatewayv2#NotFoundException``."""

    code: str | None = "NotFoundException"

    def __init__(self, data: NotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NotFoundException":
        return cls(deserialize_json(data))
