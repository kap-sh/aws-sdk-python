"""Generated from Smithy shape ``com.amazonaws.iam#CreateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.user


class CreateUserResponse(TypedDict, closed=True):
    user: NotRequired["capo_iam.types.user.User"]
    """<p>A structure with details about the new IAM user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateUserResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user" in value:
        import capo_iam.types.user

        capo_iam.types.user.serialize_query(value["user"], pairs, f"{key_prefix}User")


def deserialize_query(el: Element) -> CreateUserResponse:
    out: CreateUserResponse = {}  # type: ignore[typeddict-item]
    child_user = el.find("User")
    if child_user is not None:
        import capo_iam.types.user

        out["user"] = capo_iam.types.user.deserialize_query(child_user)
    return out
