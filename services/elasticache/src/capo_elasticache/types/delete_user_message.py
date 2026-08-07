"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteUserMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.user_id


class DeleteUserMessage(TypedDict, closed=True):
    user_id: NotRequired["capo_elasticache.types.user_id.UserId"]
    """<p>The ID of the user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteUserMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_id" in value:
        pairs.append((f"{key_prefix}UserId", str(value["user_id"])))


def deserialize_query(el: Element) -> DeleteUserMessage:
    out: DeleteUserMessage = {}  # type: ignore[typeddict-item]
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    return out
