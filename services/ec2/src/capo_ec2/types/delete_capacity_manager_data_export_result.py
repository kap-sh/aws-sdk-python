"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteCapacityManagerDataExportResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_manager_data_export_id


class DeleteCapacityManagerDataExportResult(TypedDict, closed=True):
    capacity_manager_data_export_id: NotRequired[
        "capo_ec2.types.capacity_manager_data_export_id.CapacityManagerDataExportId"
    ]
    """<p> The unique identifier of the deleted data export configuration. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteCapacityManagerDataExportResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_manager_data_export_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityManagerDataExportId",
                str(value["capacity_manager_data_export_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteCapacityManagerDataExportResult:
    out: DeleteCapacityManagerDataExportResult = {}  # type: ignore[typeddict-item]
    child_capacity_manager_data_export_id = el.find("CapacityManagerDataExportId")
    if child_capacity_manager_data_export_id is not None:
        out["capacity_manager_data_export_id"] = str(
            child_capacity_manager_data_export_id.text or ""
        )
    return out
