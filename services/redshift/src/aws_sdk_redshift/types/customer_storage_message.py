"""Generated from Smithy shape ``com.amazonaws.redshift#CustomerStorageMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.double


class CustomerStorageMessage(TypedDict):
    total_backup_size_in_mega_bytes: NotRequired["aws_sdk_redshift.types.double.Double"]
    """<p>The total amount of storage currently used for snapshots.</p>"""
    total_provisioned_storage_in_mega_bytes: NotRequired[
        "aws_sdk_redshift.types.double.Double"
    ]
    """<p>The total amount of storage currently provisioned.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomerStorageMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "total_backup_size_in_mega_bytes" in value:
        pairs.append(
            (
                f"{prefix}.TotalBackupSizeInMegaBytes",
                str(value["total_backup_size_in_mega_bytes"]),
            )
        )
    if "total_provisioned_storage_in_mega_bytes" in value:
        pairs.append(
            (
                f"{prefix}.TotalProvisionedStorageInMegaBytes",
                str(value["total_provisioned_storage_in_mega_bytes"]),
            )
        )


def deserialize_query(el: Element) -> CustomerStorageMessage:
    out: CustomerStorageMessage = {}  # type: ignore[typeddict-item]
    child_total_backup_size_in_mega_bytes = el.find("TotalBackupSizeInMegaBytes")
    if child_total_backup_size_in_mega_bytes is not None:
        out["total_backup_size_in_mega_bytes"] = float(
            child_total_backup_size_in_mega_bytes.text or ""
        )
    child_total_provisioned_storage_in_mega_bytes = el.find(
        "TotalProvisionedStorageInMegaBytes"
    )
    if child_total_provisioned_storage_in_mega_bytes is not None:
        out["total_provisioned_storage_in_mega_bytes"] = float(
            child_total_provisioned_storage_in_mega_bytes.text or ""
        )
    return out
