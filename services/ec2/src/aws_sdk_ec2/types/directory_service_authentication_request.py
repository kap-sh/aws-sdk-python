"""Generated from Smithy shape ``com.amazonaws.ec2#DirectoryServiceAuthenticationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class DirectoryServiceAuthenticationRequest(TypedDict):
    directory_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Active Directory to be used for authentication.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DirectoryServiceAuthenticationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "directory_id" in value:
        pairs.append((f"{prefix}.DirectoryId", str(value["directory_id"])))


def deserialize_ec2_query(el: Element) -> DirectoryServiceAuthenticationRequest:
    out: DirectoryServiceAuthenticationRequest = {}  # type: ignore[typeddict-item]
    child_directory_id = el.find("DirectoryId")
    if child_directory_id is not None:
        out["directory_id"] = str(child_directory_id.text or "")
    return out
