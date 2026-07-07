"""Generated from Smithy shape ``com.amazonaws.dax#ServiceLinkedRoleNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dax.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dax.types.exception_message


class ServiceLinkedRoleNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_dax.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceLinkedRoleNotFoundFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceLinkedRoleNotFoundFault_:
    out: ServiceLinkedRoleNotFoundFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ServiceLinkedRoleNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dax#ServiceLinkedRoleNotFoundFault``."""

    code: str | None = "ServiceLinkedRoleNotFoundFault"

    def __init__(self, data: ServiceLinkedRoleNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceLinkedRoleNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ServiceLinkedRoleNotFoundFault":
        return cls(deserialize_aws_json_1_1(data))
