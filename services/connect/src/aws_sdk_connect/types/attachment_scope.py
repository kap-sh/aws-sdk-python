"""Generated from Smithy shape ``com.amazonaws.connect#AttachmentScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

"""<p>The scope of the attachment. Valid values are:</p> <ul> <li> <p> <code>EMAIL</code> - Attachments for email messages.</p> </li> <li> <p> <code>CHAT</code> - Attachments for chat conversations.</p> </li> <li> <p> <code>CASE</code> - Attachments for cases.</p> </li> <li> <p> <code>TASK</code> - Attachments for tasks.</p> </li> </ul>"""
AttachmentScope: TypeAlias = Literal[
    "EMAIL",
    "CHAT",
    "CASE",
    "TASK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMAIL",
        "CHAT",
        "CASE",
        "TASK",
    )
)


def serialize_json(value: AttachmentScope) -> str:
    return value


def deserialize_json(data: str) -> AttachmentScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttachmentScope value: {data!r}")
    return cast(AttachmentScope, data)
