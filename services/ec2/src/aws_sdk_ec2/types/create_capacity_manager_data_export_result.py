"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityManagerDataExportResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_data_export_id


class CreateCapacityManagerDataExportResult(TypedDict):
    capacity_manager_data_export_id: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_data_export_id.CapacityManagerDataExportId"
    ]
    """<p> The unique identifier for the created data export configuration. Use this ID to reference the export in other API calls. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCapacityManagerDataExportResult,
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


def deserialize_ec2_query(el: Element) -> CreateCapacityManagerDataExportResult:
    out: CreateCapacityManagerDataExportResult = {}  # type: ignore[typeddict-item]
    child_capacity_manager_data_export_id = el.find("CapacityManagerDataExportId")
    if child_capacity_manager_data_export_id is not None:
        out["capacity_manager_data_export_id"] = str(
            child_capacity_manager_data_export_id.text or ""
        )
    return out
