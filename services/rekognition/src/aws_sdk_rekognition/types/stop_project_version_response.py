"""Generated from Smithy shape ``com.amazonaws.rekognition#StopProjectVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.project_version_status


class StopProjectVersionResponse(TypedDict):
    status: NotRequired[
        "aws_sdk_rekognition.types.project_version_status.ProjectVersionStatus"
    ]
    """<p>The current status of the stop operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopProjectVersionResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_rekognition.types.project_version_status

        out["Status"] = (
            aws_sdk_rekognition.types.project_version_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopProjectVersionResponse:
    out: StopProjectVersionResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_rekognition.types.project_version_status

        out["status"] = (
            aws_sdk_rekognition.types.project_version_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
