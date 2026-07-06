"""Generated from Smithy shape ``com.amazonaws.directoryservice#HybridUpdateActivities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.hybrid_update_info_entries


class HybridUpdateActivities(TypedDict, closed=True):
    self_managed_instances: NotRequired[
        "aws_sdk_directory_service.types.hybrid_update_info_entries.HybridUpdateInfoEntries"
    ]
    """<p>A list of update activities related to the self-managed instances with SSM in the self-managed instances with SSM hybrid directory configuration.</p>"""
    hybrid_administrator_account: NotRequired[
        "aws_sdk_directory_service.types.hybrid_update_info_entries.HybridUpdateInfoEntries"
    ]
    """<p>A list of update activities related to hybrid directory administrator account changes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HybridUpdateActivities) -> dict:
    out: dict = {}
    if "self_managed_instances" in value:
        import aws_sdk_directory_service.types.hybrid_update_info_entries

        out["SelfManagedInstances"] = (
            aws_sdk_directory_service.types.hybrid_update_info_entries.serialize_aws_json_1_1(
                value["self_managed_instances"]
            )
        )
    if "hybrid_administrator_account" in value:
        import aws_sdk_directory_service.types.hybrid_update_info_entries

        out["HybridAdministratorAccount"] = (
            aws_sdk_directory_service.types.hybrid_update_info_entries.serialize_aws_json_1_1(
                value["hybrid_administrator_account"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HybridUpdateActivities:
    out: HybridUpdateActivities = {}  # type: ignore[typeddict-item]
    if "SelfManagedInstances" in data:
        import aws_sdk_directory_service.types.hybrid_update_info_entries

        out["self_managed_instances"] = (
            aws_sdk_directory_service.types.hybrid_update_info_entries.deserialize_aws_json_1_1(
                data["SelfManagedInstances"]
            )
        )
    if "HybridAdministratorAccount" in data:
        import aws_sdk_directory_service.types.hybrid_update_info_entries

        out["hybrid_administrator_account"] = (
            aws_sdk_directory_service.types.hybrid_update_info_entries.deserialize_aws_json_1_1(
                data["HybridAdministratorAccount"]
            )
        )
    return out
