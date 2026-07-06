"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.id


class CreateProjectResponse(TypedDict, closed=True):
    project_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the project.</p>"""
    project_arn: "aws_sdk_iotsitewise.types.arn.ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the project, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:project/${ProjectId}</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectResponse) -> dict:
    out: dict = {}
    out["projectId"] = value["project_id"]
    out["projectArn"] = value["project_arn"]
    return out


def deserialize_json(data: dict) -> CreateProjectResponse:
    out: CreateProjectResponse = {}  # type: ignore[typeddict-item]
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("CreateProjectResponse.project_id required")
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("CreateProjectResponse.project_arn required")
    return out
