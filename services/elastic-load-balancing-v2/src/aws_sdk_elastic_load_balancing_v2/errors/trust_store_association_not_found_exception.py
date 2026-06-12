"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TrustStoreAssociationNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.error_description


class TrustStoreAssociationNotFoundException_(TypedDict):
    message: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: TrustStoreAssociationNotFoundException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> TrustStoreAssociationNotFoundException_:
    out: TrustStoreAssociationNotFoundException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TrustStoreAssociationNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancingv2#TrustStoreAssociationNotFoundException``."""

    code: str | None = "TrustStoreAssociationNotFoundException"

    def __init__(self, data: TrustStoreAssociationNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TrustStoreAssociationNotFoundException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "TrustStoreAssociationNotFoundException":
        return cls(deserialize_query(el))
