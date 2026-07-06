"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DuplicateAccessPointNameException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.error_description


class DuplicateAccessPointNameException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_elastic_load_balancing.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DuplicateAccessPointNameException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> DuplicateAccessPointNameException_:
    out: DuplicateAccessPointNameException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DuplicateAccessPointNameException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancing#DuplicateAccessPointNameException``."""

    code: str | None = "DuplicateAccessPointNameException"

    def __init__(self, data: DuplicateAccessPointNameException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateAccessPointNameException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DuplicateAccessPointNameException":
        return cls(deserialize_query(el))
