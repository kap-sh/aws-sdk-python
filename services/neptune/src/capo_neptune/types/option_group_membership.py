"""Generated from Smithy shape ``com.amazonaws.neptune#OptionGroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.string


class OptionGroupMembership(TypedDict, closed=True):
    option_group_name: NotRequired["capo_neptune.types.string.String"]
    """<p>Not supported by Neptune.</p>"""
    status: NotRequired["capo_neptune.types.string.String"]
    """<p>Not supported by Neptune.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroupMembership, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "option_group_name" in value:
        pairs.append((f"{prefix}.OptionGroupName", str(value["option_group_name"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> OptionGroupMembership:
    out: OptionGroupMembership = {}  # type: ignore[typeddict-item]
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
