"""Generated from Smithy shape ``com.amazonaws.iam#ErrorDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.string_type


class ErrorDetails(TypedDict):
    message: "aws_sdk_iam.types.string_type.stringType"
    """<p>Detailed information about the reason that the operation failed.</p>"""
    code: "aws_sdk_iam.types.string_type.stringType"
    """<p>The error code associated with the operation failure.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ErrorDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Message", str(value["message"])))
    pairs.append((f"{prefix}.Code", str(value["code"])))


def deserialize_query(el: Element) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    else:
        raise DeserializationError("ErrorDetails.message required")
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    else:
        raise DeserializationError("ErrorDetails.code required")
    return out
