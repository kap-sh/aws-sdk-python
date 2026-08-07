"""Generated from Smithy shape ``com.amazonaws.docdb#AvailabilityZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.string


class AvailabilityZone(TypedDict, closed=True):
    name: NotRequired["capo_docdb.types.string.String"]
    """<p>The name of the Availability Zone.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityZone, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))


def deserialize_query(el: Element) -> AvailabilityZone:
    out: AvailabilityZone = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
