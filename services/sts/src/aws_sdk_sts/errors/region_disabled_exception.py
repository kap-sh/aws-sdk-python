"""Generated from Smithy shape ``com.amazonaws.sts#RegionDisabledException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sts._protocol.xml import Element
from aws_sdk_sts.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sts.types.region_disabled_message


class RegionDisabledException_(TypedDict):
    message: NotRequired[
        "aws_sdk_sts.types.region_disabled_message.regionDisabledMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: RegionDisabledException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> RegionDisabledException_:
    out: RegionDisabledException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class RegionDisabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sts#RegionDisabledException``."""

    code: str | None = "RegionDisabledException"

    def __init__(self, data: RegionDisabledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RegionDisabledException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "RegionDisabledException":
        return cls(deserialize_query(el))
