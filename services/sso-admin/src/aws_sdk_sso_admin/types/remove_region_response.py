"""Generated from Smithy shape ``com.amazonaws.ssoadmin#RemoveRegionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.region_status


class RemoveRegionResponse(TypedDict, closed=True):
    status: NotRequired["aws_sdk_sso_admin.types.region_status.RegionStatus"]
    """<p>The status of the Region after the remove operation. The status is REMOVING when the asynchronous workflow is in progress. The Region record is deleted when the workflow completes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveRegionResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sso_admin.types.region_status

        out["Status"] = aws_sdk_sso_admin.types.region_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveRegionResponse:
    out: RemoveRegionResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sso_admin.types.region_status

        out["status"] = aws_sdk_sso_admin.types.region_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
