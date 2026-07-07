"""Generated from Smithy shape ``com.amazonaws.elasticache#AvailabilityZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class AvailabilityZone(TypedDict, closed=True):
    name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the Availability Zone.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityZone, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))


def deserialize_query(el: Element) -> AvailabilityZone:
    out: AvailabilityZone = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
