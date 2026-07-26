"""Generated from Smithy shape ``com.amazonaws.redshift#SupportedPlatform``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class SupportedPlatform(TypedDict, closed=True):
    name: NotRequired["capo_redshift.types.string.String"]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SupportedPlatform, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))


def deserialize_query(el: Element) -> SupportedPlatform:
    out: SupportedPlatform = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
