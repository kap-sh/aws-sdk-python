"""Generated from Smithy shape ``com.amazonaws.elasticache#InvalidParameterCombinationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.aws_query_error_message


class InvalidParameterCombinationException_(TypedDict):
    message: NotRequired[
        "aws_sdk_elasticache.types.aws_query_error_message.AwsQueryErrorMessage"
    ]
    """<p>Two or more parameters that must not be used together were used together.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidParameterCombinationException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidParameterCombinationException_:
    out: InvalidParameterCombinationException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidParameterCombinationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticache#InvalidParameterCombinationException``."""

    code: str | None = "InvalidParameterCombinationException"

    def __init__(self, data: InvalidParameterCombinationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterCombinationException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidParameterCombinationException":
        return cls(deserialize_query(el))
