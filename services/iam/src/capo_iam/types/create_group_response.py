"""Generated from Smithy shape ``com.amazonaws.iam#CreateGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.group


class CreateGroupResponse(TypedDict, closed=True):
    group: "capo_iam.types.group.Group"
    """<p>A structure containing details about the new group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateGroupResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.group

    capo_iam.types.group.serialize_query(value["group"], pairs, f"{prefix}.Group")


def deserialize_query(el: Element) -> CreateGroupResponse:
    out: CreateGroupResponse = {}  # type: ignore[typeddict-item]
    child_group = el.find("Group")
    if child_group is not None:
        import capo_iam.types.group

        out["group"] = capo_iam.types.group.deserialize_query(child_group)
    else:
        raise DeserializationError("CreateGroupResponse.group required")
    return out
