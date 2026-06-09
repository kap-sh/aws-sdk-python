"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group_name


class PlacementResponse(TypedDict):
    group_name: NotRequired["aws_sdk_ec2.types.placement_group_name.PlacementGroupName"]
    """<p>The name of the placement group that the instance is in.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PlacementResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "group_name" in value:
        pairs.append((f"{prefix}.GroupName", str(value["group_name"])))


def deserialize_ec2_query(el: Element) -> PlacementResponse:
    out: PlacementResponse = {}  # type: ignore[typeddict-item]
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    return out
