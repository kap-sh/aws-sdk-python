"""Generated from Smithy shape ``com.amazonaws.iam#OrganizationNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.exception_message


class OrganizationNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_iam.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: OrganizationNotFoundException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> OrganizationNotFoundException_:
    out: OrganizationNotFoundException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class OrganizationNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#OrganizationNotFoundException``."""

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
    def from_query(cls, el: Element) -> "OrganizationNotFoundException":
        return cls(deserialize_query(el))
