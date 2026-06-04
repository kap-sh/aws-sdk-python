"""Generated from Smithy shape ``com.amazonaws.iam#CreateUserResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.user


class CreateUserResponse(TypedDict):
    user: NotRequired["aws_sdk_iam.types.user.User"]
    """<p>A structure with details about the new IAM user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateUserResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user" in value:
        import aws_sdk_iam.types.user

        aws_sdk_iam.types.user.serialize_query(value["user"], pairs, f"{prefix}.User")


def deserialize_query(el: Element) -> CreateUserResponse:
    out: CreateUserResponse = {}  # type: ignore[typeddict-item]
    child_user = el.find("User")
    if child_user is not None:
        import aws_sdk_iam.types.user

        out["user"] = aws_sdk_iam.types.user.deserialize_query(child_user)
    return out
