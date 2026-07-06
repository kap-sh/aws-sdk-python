"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneGeography``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AvailabilityZoneGeography(TypedDict, closed=True):
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the geography, for example, <code>United States of America</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailabilityZoneGeography, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))


def deserialize_ec2_query(el: Element) -> AvailabilityZoneGeography:
    out: AvailabilityZoneGeography = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
