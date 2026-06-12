"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncDestinationDataSharing``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.resource_data_sync_destination_data_sharing_type


class ResourceDataSyncDestinationDataSharing(TypedDict):
    destination_data_sharing_type: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_destination_data_sharing_type.ResourceDataSyncDestinationDataSharingType"
    ]
    """<p>The sharing data type. Only <code>Organization</code> is supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncDestinationDataSharing) -> dict:
    out: dict = {}
    if "destination_data_sharing_type" in value:
        out["DestinationDataSharingType"] = value["destination_data_sharing_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncDestinationDataSharing:
    out: ResourceDataSyncDestinationDataSharing = {}  # type: ignore[typeddict-item]
    if "DestinationDataSharingType" in data:
        out["destination_data_sharing_type"] = data["DestinationDataSharingType"]
    return out
