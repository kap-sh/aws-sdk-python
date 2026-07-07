"""Generated from Smithy shape ``com.amazonaws.sns#BatchResultErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.boolean
    import aws_sdk_sns.types.string


class BatchResultErrorEntry(TypedDict, closed=True):
    id: "aws_sdk_sns.types.string.String"
    """<p>The <code>Id</code> of an entry in a batch request</p>"""
    code: "aws_sdk_sns.types.string.String"
    """<p>An error code representing why the action failed on this entry.</p>"""
    message: NotRequired["aws_sdk_sns.types.string.String"]
    """<p>A message explaining why the action failed on this entry.</p>"""
    sender_fault: "aws_sdk_sns.types.boolean.boolean"
    """<p>Specifies whether the error happened due to the caller of the batch API action.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchResultErrorEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Id", str(value["id"])))
    pairs.append((f"{prefix}.Code", str(value["code"])))
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))
    pairs.append(
        (
            f"{prefix}.SenderFault",
            "true" if value.get("sender_fault", False) else "false",
        )
    )


def deserialize_query(el: Element) -> BatchResultErrorEntry:
    out: BatchResultErrorEntry = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("BatchResultErrorEntry.id required")
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    else:
        raise DeserializationError("BatchResultErrorEntry.code required")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_sender_fault = el.find("SenderFault")
    if child_sender_fault is not None:
        out["sender_fault"] = (child_sender_fault.text or "").lower() == "true"
    else:
        out["sender_fault"] = False
    return out
