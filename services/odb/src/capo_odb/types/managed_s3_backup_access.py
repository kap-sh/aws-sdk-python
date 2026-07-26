"""Generated from Smithy shape ``com.amazonaws.odb#ManagedS3BackupAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.managed_resource_status
    import capo_odb.types.string_list


class ManagedS3BackupAccess(TypedDict, closed=True):
    status: NotRequired["capo_odb.types.managed_resource_status.ManagedResourceStatus"]
    """<p>The status of the managed Amazon S3 backup access.</p>"""
    ipv4_addresses: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The IPv4 addresses for the managed Amazon S3 backup access.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ManagedS3BackupAccess) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_odb.types.managed_resource_status

        out["status"] = capo_odb.types.managed_resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "ipv4_addresses" in value:
        import capo_odb.types.string_list

        out["ipv4Addresses"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["ipv4_addresses"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ManagedS3BackupAccess:
    out: ManagedS3BackupAccess = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_odb.types.managed_resource_status

        out["status"] = capo_odb.types.managed_resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "ipv4Addresses" in data:
        import capo_odb.types.string_list

        out["ipv4_addresses"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["ipv4Addresses"]
        )
    return out
