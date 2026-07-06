"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#PolicyTypeNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.error_description


class PolicyTypeNotFoundException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_elastic_load_balancing.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyTypeNotFoundException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> PolicyTypeNotFoundException_:
    out: PolicyTypeNotFoundException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class PolicyTypeNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancing#PolicyTypeNotFoundException``."""

    code: str | None = "PolicyTypeNotFoundException"

    def __init__(self, data: PolicyTypeNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyTypeNotFoundException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "PolicyTypeNotFoundException":
        return cls(deserialize_query(el))
