"""Generated from Smithy shape ``com.amazonaws.iam#FeatureDisabledException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.feature_disabled_message


class FeatureDisabledException_(TypedDict):
    message: NotRequired[
        "aws_sdk_iam.types.feature_disabled_message.FeatureDisabledMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: FeatureDisabledException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> FeatureDisabledException_:
    out: FeatureDisabledException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class FeatureDisabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#FeatureDisabledException``."""

    code: str | None = "FeatureDisabledException"

    def __init__(self, data: FeatureDisabledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FeatureDisabledException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "FeatureDisabledException":
        return cls(deserialize_query(el))
