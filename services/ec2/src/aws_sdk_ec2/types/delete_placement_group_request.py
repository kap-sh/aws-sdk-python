"""Generated from Smithy shape ``com.amazonaws.ec2#DeletePlacementGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.placement_group_name_with_resolver


class DeletePlacementGroupRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    group_name: NotRequired[
        "aws_sdk_ec2.types.placement_group_name_with_resolver.PlacementGroupNameWithResolver"
    ]
    """<p>The name of the placement group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeletePlacementGroupRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "group_name" in value:
        pairs.append((f"{prefix}.GroupName", str(value["group_name"])))


def deserialize_ec2_query(el: Element) -> DeletePlacementGroupRequest:
    out: DeletePlacementGroupRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    return out
