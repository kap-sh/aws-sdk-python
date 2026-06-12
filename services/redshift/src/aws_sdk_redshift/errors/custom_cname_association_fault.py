"""Generated from Smithy shape ``com.amazonaws.redshift#CustomCnameAssociationFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.exception_message


class CustomCnameAssociationFault_(TypedDict):
    message: NotRequired["aws_sdk_redshift.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomCnameAssociationFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> CustomCnameAssociationFault_:
    out: CustomCnameAssociationFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CustomCnameAssociationFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.redshift#CustomCnameAssociationFault``."""

    code: str | None = "CustomCnameAssociationFault"

    def __init__(self, data: CustomCnameAssociationFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomCnameAssociationFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "CustomCnameAssociationFault":
        return cls(deserialize_query(el))
