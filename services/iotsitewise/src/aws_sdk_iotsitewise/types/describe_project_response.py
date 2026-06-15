"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeProjectResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.description
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.timestamp


class DescribeProjectResponse(TypedDict):
    project_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the project.</p>"""
    project_arn: "aws_sdk_iotsitewise.types.arn.ARN"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the project, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:project/${ProjectId}</code> </p>"""
    project_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the project.</p>"""
    portal_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the portal that the project is in.</p>"""
    project_description: NotRequired[
        "aws_sdk_iotsitewise.types.description.Description"
    ]
    """<p>The project's description.</p>"""
    project_creation_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the project was created, in Unix epoch time.</p>"""
    project_last_update_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the project was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProjectResponse) -> dict:
    out: dict = {}
    out["projectId"] = value["project_id"]
    out["projectArn"] = value["project_arn"]
    out["projectName"] = value["project_name"]
    out["portalId"] = value["portal_id"]
    if "project_description" in value:
        out["projectDescription"] = value["project_description"]
    import aws_sdk_iotsitewise.types.timestamp

    out["projectCreationDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["project_creation_date"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["projectLastUpdateDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["project_last_update_date"]
    )
    return out


def deserialize_json(data: dict) -> DescribeProjectResponse:
    out: DescribeProjectResponse = {}  # type: ignore[typeddict-item]
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("DescribeProjectResponse.project_id required")
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("DescribeProjectResponse.project_arn required")
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("DescribeProjectResponse.project_name required")
    if "portalId" in data:
        out["portal_id"] = data["portalId"]
    else:
        raise DeserializationError("DescribeProjectResponse.portal_id required")
    if "projectDescription" in data:
        out["project_description"] = data["projectDescription"]
    if "projectCreationDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["project_creation_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["projectCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeProjectResponse.project_creation_date required"
        )
    if "projectLastUpdateDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["project_last_update_date"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["projectLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeProjectResponse.project_last_update_date required"
        )
    return out
