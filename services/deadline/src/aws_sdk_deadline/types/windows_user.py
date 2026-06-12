"""Generated from Smithy shape ``com.amazonaws.deadline#WindowsUser``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.string


class WindowsUser(TypedDict):
    user: "aws_sdk_deadline.types.string.String"
    """<p>The user.</p>"""
    password_arn: "aws_sdk_deadline.types.string.String"
    """<p>The password ARN for the Windows user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WindowsUser) -> dict:
    out: dict = {}
    out["user"] = value["user"]
    out["passwordArn"] = value["password_arn"]
    return out


def deserialize_json(data: dict) -> WindowsUser:
    out: WindowsUser = {}  # type: ignore[typeddict-item]
    if "user" in data:
        out["user"] = data["user"]
    else:
        raise DeserializationError("WindowsUser.user required")
    if "passwordArn" in data:
        out["password_arn"] = data["passwordArn"]
    else:
        raise DeserializationError("WindowsUser.password_arn required")
    return out
