"""Generated from Smithy shape ``com.amazonaws.ses#InvalidLambdaFunctionException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ses.types.amazon_resource_name
    import aws_sdk_ses.types.error_message


class InvalidLambdaFunctionException_(TypedDict):
    function_arn: NotRequired[
        "aws_sdk_ses.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>Indicates that the ARN of the function was not found.</p>"""
    message: NotRequired["aws_sdk_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidLambdaFunctionException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "function_arn" in value:
        pairs.append((f"{prefix}.FunctionArn", str(value["function_arn"])))
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidLambdaFunctionException_:
    out: InvalidLambdaFunctionException_ = {}  # type: ignore[typeddict-item]
    child_function_arn = el.find("FunctionArn")
    if child_function_arn is not None:
        out["function_arn"] = str(child_function_arn.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidLambdaFunctionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#InvalidLambdaFunctionException``."""

    code: str | None = "InvalidLambdaFunctionException"

    def __init__(self, data: InvalidLambdaFunctionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidLambdaFunctionException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidLambdaFunctionException":
        return cls(deserialize_query(el))
