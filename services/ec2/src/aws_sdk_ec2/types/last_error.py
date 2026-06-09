"""Generated from Smithy shape ``com.amazonaws.ec2#LastError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class LastError(TypedDict):
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The error message for the VPC endpoint error.</p>"""
    code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The error code for the VPC endpoint error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LastError, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))
    if "code" in value:
        pairs.append((f"{prefix}.Code", str(value["code"])))


def deserialize_ec2_query(el: Element) -> LastError:
    out: LastError = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    return out
