"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#S3SubscriptionRequiredException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.exception_message


class S3SubscriptionRequiredException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_elastic_beanstalk.types.exception_message.ExceptionMessage"
    ]
    """<p>The exception error message.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: S3SubscriptionRequiredException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> S3SubscriptionRequiredException_:
    out: S3SubscriptionRequiredException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class S3SubscriptionRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticbeanstalk#S3SubscriptionRequiredException``."""

    code: str | None = "S3SubscriptionRequiredException"

    def __init__(self, data: S3SubscriptionRequiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="S3SubscriptionRequiredException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "S3SubscriptionRequiredException":
        return cls(deserialize_query(el))
