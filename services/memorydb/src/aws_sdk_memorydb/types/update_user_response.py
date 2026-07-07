"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.user


class UpdateUserResponse(TypedDict, closed=True):
    user: NotRequired["aws_sdk_memorydb.types.user.User"]
    """<p>The updated user</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import aws_sdk_memorydb.types.user

        out["User"] = aws_sdk_memorydb.types.user.serialize_aws_json_1_1(value["user"])
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserResponse:
    out: UpdateUserResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import aws_sdk_memorydb.types.user

        out["user"] = aws_sdk_memorydb.types.user.deserialize_aws_json_1_1(data["User"])
    return out
