"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteCapacityManagerDataExportRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_manager_data_export_id


class DeleteCapacityManagerDataExportRequest(TypedDict):
    capacity_manager_data_export_id: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_data_export_id.CapacityManagerDataExportId"
    ]
    """<p> The unique identifier of the data export configuration to delete. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteCapacityManagerDataExportRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_manager_data_export_id" in value:
        pairs.append(
            (
                f"{prefix}.CapacityManagerDataExportId",
                str(value["capacity_manager_data_export_id"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteCapacityManagerDataExportRequest:
    out: DeleteCapacityManagerDataExportRequest = {}  # type: ignore[typeddict-item]
    child_capacity_manager_data_export_id = el.find("CapacityManagerDataExportId")
    if child_capacity_manager_data_export_id is not None:
        out["capacity_manager_data_export_id"] = str(
            child_capacity_manager_data_export_id.text or ""
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
