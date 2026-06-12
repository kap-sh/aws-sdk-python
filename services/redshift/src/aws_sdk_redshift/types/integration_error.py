"""Generated from Smithy shape ``com.amazonaws.redshift#IntegrationError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class IntegrationError(TypedDict):
    error_code: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The error code of an inbound integration error.</p>"""
    error_message: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The error message of an inbound integration error.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: IntegrationError, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "error_code" in value:
        pairs.append((f"{prefix}.ErrorCode", str(value["error_code"])))
    if "error_message" in value:
        pairs.append((f"{prefix}.ErrorMessage", str(value["error_message"])))


def deserialize_query(el: Element) -> IntegrationError:
    out: IntegrationError = {}  # type: ignore[typeddict-item]
    child_error_code = el.find("ErrorCode")
    if child_error_code is not None:
        out["error_code"] = str(child_error_code.text or "")
    child_error_message = el.find("ErrorMessage")
    if child_error_message is not None:
        out["error_message"] = str(child_error_message.text or "")
    return out
