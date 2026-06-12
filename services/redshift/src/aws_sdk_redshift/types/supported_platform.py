"""Generated from Smithy shape ``com.amazonaws.redshift#SupportedPlatform``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class SupportedPlatform(TypedDict):
    name: NotRequired["aws_sdk_redshift.types.string.String"]
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
