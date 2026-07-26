"""Generated from Smithy shape ``com.amazonaws.ses#ProductionAccessNotGrantedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import ServiceError

if TYPE_CHECKING:
    import capo_ses.types.error_message


class ProductionAccessNotGrantedException_(TypedDict, closed=True):
    message: NotRequired["capo_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ProductionAccessNotGrantedException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> ProductionAccessNotGrantedException_:
    out: ProductionAccessNotGrantedException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ProductionAccessNotGrantedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#ProductionAccessNotGrantedException``."""

    code: str | None = "ProductionAccessNotGrantedException"

    def __init__(self, data: ProductionAccessNotGrantedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ProductionAccessNotGrantedException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ProductionAccessNotGrantedException":
        return cls(deserialize_query(el))
