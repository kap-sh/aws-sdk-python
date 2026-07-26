"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSUserOrGroupQuota``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.integer_no_max
    import capo_fsx.types.open_zfs_quota_type


class OpenZFSUserOrGroupQuota(TypedDict, closed=True):
    type: NotRequired["capo_fsx.types.open_zfs_quota_type.OpenZFSQuotaType"]
    """<p>Specifies whether the quota applies to a user or group.</p>"""
    id: NotRequired["capo_fsx.types.integer_no_max.IntegerNoMax"]
    """<p>The ID of the user or group that the quota applies to.</p>"""
    storage_capacity_quota_gi_b: NotRequired[
        "capo_fsx.types.integer_no_max.IntegerNoMax"
    ]
    """<p>The user or group's storage quota, in gibibytes (GiB).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSUserOrGroupQuota) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_fsx.types.open_zfs_quota_type

        out["Type"] = capo_fsx.types.open_zfs_quota_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "storage_capacity_quota_gi_b" in value:
        out["StorageCapacityQuotaGiB"] = value["storage_capacity_quota_gi_b"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenZFSUserOrGroupQuota:
    out: OpenZFSUserOrGroupQuota = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_fsx.types.open_zfs_quota_type

        out["type"] = capo_fsx.types.open_zfs_quota_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "StorageCapacityQuotaGiB" in data:
        out["storage_capacity_quota_gi_b"] = data["StorageCapacityQuotaGiB"]
    return out
