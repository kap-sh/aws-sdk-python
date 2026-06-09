"""Generated from Smithy shape ``com.amazonaws.iam#CreateGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.group


class CreateGroupResponse(TypedDict):
    group: "aws_sdk_iam.types.group.Group"
    """<p>A structure containing details about the new group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateGroupResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.group

    aws_sdk_iam.types.group.serialize_query(value["group"], pairs, f"{prefix}.Group")


def deserialize_query(el: Element) -> CreateGroupResponse:
    out: CreateGroupResponse = {}  # type: ignore[typeddict-item]
    child_group = el.find("Group")
    if child_group is not None:
        import aws_sdk_iam.types.group

        out["group"] = aws_sdk_iam.types.group.deserialize_query(child_group)
    else:
        raise DeserializationError("CreateGroupResponse.group required")
    return out
