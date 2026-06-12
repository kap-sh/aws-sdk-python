"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformVersionStillReferencedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.exception_message


class PlatformVersionStillReferencedException_(TypedDict):
    message: NotRequired[
        "aws_sdk_elastic_beanstalk.types.exception_message.ExceptionMessage"
    ]
    """<p>The exception error message.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformVersionStillReferencedException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> PlatformVersionStillReferencedException_:
    out: PlatformVersionStillReferencedException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class PlatformVersionStillReferencedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformVersionStillReferencedException``."""

    code: str | None = "PlatformVersionStillReferencedException"

    def __init__(self, data: PlatformVersionStillReferencedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PlatformVersionStillReferencedException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "PlatformVersionStillReferencedException":
        return cls(deserialize_query(el))
