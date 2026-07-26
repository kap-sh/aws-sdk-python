"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.project_status


class DeleteProjectResponse(TypedDict, closed=True):
    status: NotRequired["capo_rekognition.types.project_status.ProjectStatus"]
    """<p>The current status of the delete project operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProjectResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_rekognition.types.project_status

        out["Status"] = capo_rekognition.types.project_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProjectResponse:
    out: DeleteProjectResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_rekognition.types.project_status

        out["status"] = capo_rekognition.types.project_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
