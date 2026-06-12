"""Generated from Smithy shape ``com.amazonaws.memorydb#PendingModifiedServiceUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.service_update_status
    import aws_sdk_memorydb.types.string


class PendingModifiedServiceUpdate(TypedDict):
    service_update_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The unique ID of the service update</p>"""
    status: NotRequired[
        "aws_sdk_memorydb.types.service_update_status.ServiceUpdateStatus"
    ]
    """<p>The status of the service update</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingModifiedServiceUpdate) -> dict:
    out: dict = {}
    if "service_update_name" in value:
        out["ServiceUpdateName"] = value["service_update_name"]
    if "status" in value:
        import aws_sdk_memorydb.types.service_update_status

        out["Status"] = (
            aws_sdk_memorydb.types.service_update_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PendingModifiedServiceUpdate:
    out: PendingModifiedServiceUpdate = {}  # type: ignore[typeddict-item]
    if "ServiceUpdateName" in data:
        out["service_update_name"] = data["ServiceUpdateName"]
    if "Status" in data:
        import aws_sdk_memorydb.types.service_update_status

        out["status"] = (
            aws_sdk_memorydb.types.service_update_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
