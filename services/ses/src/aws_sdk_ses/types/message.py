"""Generated from Smithy shape ``com.amazonaws.ses#Message``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.body
    import aws_sdk_ses.types.content


class Message(TypedDict):
    subject: "aws_sdk_ses.types.content.Content"
    """<p>The subject of the message: A short summary of the content, which appears in the recipient's inbox.</p>"""
    body: "aws_sdk_ses.types.body.Body"
    """<p>The message body.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Message, pairs: list[tuple[str, str]], prefix: str) -> None:
    import aws_sdk_ses.types.content

    aws_sdk_ses.types.content.serialize_query(
        value["subject"], pairs, f"{prefix}.Subject"
    )
    import aws_sdk_ses.types.body

    aws_sdk_ses.types.body.serialize_query(value["body"], pairs, f"{prefix}.Body")


def deserialize_query(el: Element) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    child_subject = el.find("Subject")
    if child_subject is not None:
        import aws_sdk_ses.types.content

        out["subject"] = aws_sdk_ses.types.content.deserialize_query(child_subject)
    else:
        raise DeserializationError("Message.subject required")
    child_body = el.find("Body")
    if child_body is not None:
        import aws_sdk_ses.types.body

        out["body"] = aws_sdk_ses.types.body.deserialize_query(child_body)
    else:
        raise DeserializationError("Message.body required")
    return out
