"""Generated from Smithy shape ``com.amazonaws.connect#DescribeUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.user


class DescribeUserResponse(TypedDict, closed=True):
    user: NotRequired["aws_sdk_connect.types.user.User"]
    """<p>Information about the user account and configuration settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import aws_sdk_connect.types.user

        out["User"] = aws_sdk_connect.types.user.serialize_json(value["user"])
    return out


def deserialize_json(data: dict) -> DescribeUserResponse:
    out: DescribeUserResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import aws_sdk_connect.types.user

        out["user"] = aws_sdk_connect.types.user.deserialize_json(data["User"])
    return out
