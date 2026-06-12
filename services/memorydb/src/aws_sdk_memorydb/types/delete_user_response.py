"""Generated from Smithy shape ``com.amazonaws.memorydb#DeleteUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.user


class DeleteUserResponse(TypedDict):
    user: NotRequired["aws_sdk_memorydb.types.user.User"]
    """<p>The user object that has been deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import aws_sdk_memorydb.types.user

        out["User"] = aws_sdk_memorydb.types.user.serialize_aws_json_1_1(value["user"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserResponse:
    out: DeleteUserResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import aws_sdk_memorydb.types.user

        out["user"] = aws_sdk_memorydb.types.user.deserialize_aws_json_1_1(data["User"])
    return out
