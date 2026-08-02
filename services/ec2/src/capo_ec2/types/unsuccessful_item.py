"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.unsuccessful_item_error


class UnsuccessfulItem(TypedDict, closed=True):
    error: NotRequired["capo_ec2.types.unsuccessful_item_error.UnsuccessfulItemError"]
    """<p>Information about the error.</p>"""
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnsuccessfulItem, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "error" in value:
        import capo_ec2.types.unsuccessful_item_error

        capo_ec2.types.unsuccessful_item_error.serialize_ec2_query(
            value["error"], pairs, f"{key_prefix}Error"
        )
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))


def deserialize_ec2_query(el: Element) -> UnsuccessfulItem:
    out: UnsuccessfulItem = {}  # type: ignore[typeddict-item]
    child_error = el.find("Error")
    if child_error is not None:
        import capo_ec2.types.unsuccessful_item_error

        out["error"] = capo_ec2.types.unsuccessful_item_error.deserialize_ec2_query(
            child_error
        )
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    return out
