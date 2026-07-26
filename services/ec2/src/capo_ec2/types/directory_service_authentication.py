"""Generated from Smithy shape ``com.amazonaws.ec2#DirectoryServiceAuthentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class DirectoryServiceAuthentication(TypedDict, closed=True):
    directory_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Active Directory used for authentication.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DirectoryServiceAuthentication, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "directory_id" in value:
        pairs.append((f"{prefix}.DirectoryId", str(value["directory_id"])))


def deserialize_ec2_query(el: Element) -> DirectoryServiceAuthentication:
    out: DirectoryServiceAuthentication = {}  # type: ignore[typeddict-item]
    child_directory_id = el.find("DirectoryId")
    if child_directory_id is not None:
        out["directory_id"] = str(child_directory_id.text or "")
    return out
