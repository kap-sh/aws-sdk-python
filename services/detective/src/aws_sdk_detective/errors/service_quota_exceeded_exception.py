"""Generated from Smithy shape ``com.amazonaws.detective#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_detective.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_detective.types.error_message
    import aws_sdk_detective.types.resource_list


class ServiceQuotaExceededException_(TypedDict):
    message: NotRequired["aws_sdk_detective.types.error_message.ErrorMessage"]
    resources: NotRequired["aws_sdk_detective.types.resource_list.ResourceList"]
    """<p>The type of resource that has exceeded the service quota.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resources" in value:
        import aws_sdk_detective.types.resource_list

        out["Resources"] = aws_sdk_detective.types.resource_list.serialize_json(
            value["resources"]
        )
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Resources" in data:
        import aws_sdk_detective.types.resource_list

        out["resources"] = aws_sdk_detective.types.resource_list.deserialize_json(
            data["Resources"]
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.detective#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(self, data: ServiceQuotaExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceQuotaExceededException":
        return cls(deserialize_json(data))
