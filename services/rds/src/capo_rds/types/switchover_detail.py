"""Generated from Smithy shape ``com.amazonaws.rds#SwitchoverDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.database_arn
    import capo_rds.types.switchover_detail_status


class SwitchoverDetail(TypedDict, closed=True):
    source_member: NotRequired["capo_rds.types.database_arn.DatabaseArn"]
    """<p>The Amazon Resource Name (ARN) of a resource in the blue environment.</p>"""
    target_member: NotRequired["capo_rds.types.database_arn.DatabaseArn"]
    """<p>The Amazon Resource Name (ARN) of a resource in the green environment.</p>"""
    status: NotRequired[
        "capo_rds.types.switchover_detail_status.SwitchoverDetailStatus"
    ]
    """<p>The switchover status of a resource in a blue/green deployment.</p> <p>Values:</p> <ul> <li> <p> <code>PROVISIONING</code> - The resource is being prepared to switch over.</p> </li> <li> <p> <code>AVAILABLE</code> - The resource is ready to switch over.</p> </li> <li> <p> <code>SWITCHOVER_IN_PROGRESS</code> - The resource is being switched over.</p> </li> <li> <p> <code>SWITCHOVER_COMPLETED</code> - The resource has been switched over.</p> </li> <li> <p> <code>SWITCHOVER_FAILED</code> - The resource attempted to switch over but failed.</p> </li> <li> <p> <code>MISSING_SOURCE</code> - The source resource has been deleted.</p> </li> <li> <p> <code>MISSING_TARGET</code> - The target resource has been deleted.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SwitchoverDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_member" in value:
        pairs.append((f"{prefix}.SourceMember", str(value["source_member"])))
    if "target_member" in value:
        pairs.append((f"{prefix}.TargetMember", str(value["target_member"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> SwitchoverDetail:
    out: SwitchoverDetail = {}  # type: ignore[typeddict-item]
    child_source_member = el.find("SourceMember")
    if child_source_member is not None:
        out["source_member"] = str(child_source_member.text or "")
    child_target_member = el.find("TargetMember")
    if child_target_member is not None:
        out["target_member"] = str(child_target_member.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
