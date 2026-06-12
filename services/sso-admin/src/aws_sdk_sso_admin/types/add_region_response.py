"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AddRegionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.region_status


class AddRegionResponse(TypedDict):
    status: NotRequired["aws_sdk_sso_admin.types.region_status.RegionStatus"]
    """<p>The status of the Region after the Add operation. The status is ADDING when the asynchronous workflow is in progress and changes to ACTIVE when complete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddRegionResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sso_admin.types.region_status

        out["Status"] = aws_sdk_sso_admin.types.region_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddRegionResponse:
    out: AddRegionResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sso_admin.types.region_status

        out["status"] = aws_sdk_sso_admin.types.region_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
