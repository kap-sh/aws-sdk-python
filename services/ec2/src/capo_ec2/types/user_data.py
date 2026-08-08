"""Generated from Smithy shape ``com.amazonaws.ec2#UserData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class UserData(TypedDict, closed=True):
    data: NotRequired["capo_ec2.types.string.String"]
    """<p>The user data. If you are using an Amazon Web Services SDK or command line tool, Base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide Base64-encoded text.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UserData, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "data" in value:
        pairs.append((f"{key_prefix}Data", str(value["data"])))


def deserialize_ec2_query(el: Element) -> UserData:
    out: UserData = {}  # type: ignore[typeddict-item]
    child_data = el.find("data")
    if child_data is not None:
        out["data"] = str(child_data.text or "")
    return out
