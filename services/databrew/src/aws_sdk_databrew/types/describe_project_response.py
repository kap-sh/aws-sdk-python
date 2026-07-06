"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.arn
    import aws_sdk_databrew.types.created_by
    import aws_sdk_databrew.types.dataset_name
    import aws_sdk_databrew.types.date
    import aws_sdk_databrew.types.last_modified_by
    import aws_sdk_databrew.types.opened_by
    import aws_sdk_databrew.types.project_name
    import aws_sdk_databrew.types.recipe_name
    import aws_sdk_databrew.types.sample
    import aws_sdk_databrew.types.session_status
    import aws_sdk_databrew.types.tag_map


class DescribeProjectResponse(TypedDict, closed=True):
    create_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the project was created.</p>"""
    created_by: NotRequired["aws_sdk_databrew.types.created_by.CreatedBy"]
    """<p>The identifier (user name) of the user who created the project.</p>"""
    dataset_name: NotRequired["aws_sdk_databrew.types.dataset_name.DatasetName"]
    """<p>The dataset associated with the project.</p>"""
    last_modified_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the project was last modified.</p>"""
    last_modified_by: NotRequired[
        "aws_sdk_databrew.types.last_modified_by.LastModifiedBy"
    ]
    """<p>The identifier (user name) of the user who last modified the project.</p>"""
    name: "aws_sdk_databrew.types.project_name.ProjectName"
    """<p>The name of the project.</p>"""
    recipe_name: NotRequired["aws_sdk_databrew.types.recipe_name.RecipeName"]
    """<p>The recipe associated with this job.</p>"""
    resource_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the project.</p>"""
    sample: NotRequired["aws_sdk_databrew.types.sample.Sample"]
    role_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The ARN of the Identity and Access Management (IAM) role to be assumed when DataBrew runs the job.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags associated with this project.</p>"""
    session_status: NotRequired["aws_sdk_databrew.types.session_status.SessionStatus"]
    """<p>Describes the current state of the session:</p> <ul> <li> <p> <code>PROVISIONING</code> - allocating resources for the session.</p> </li> <li> <p> <code>INITIALIZING</code> - getting the session ready for first use.</p> </li> <li> <p> <code>ASSIGNED</code> - the session is ready for use.</p> </li> </ul>"""
    opened_by: NotRequired["aws_sdk_databrew.types.opened_by.OpenedBy"]
    """<p>The identifier (user name) of the user that opened the project for use. </p>"""
    open_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time when the project was opened. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProjectResponse) -> dict:
    out: dict = {}
    if "create_date" in value:
        import aws_sdk_databrew.types.date

        out["CreateDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["create_date"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "last_modified_date" in value:
        import aws_sdk_databrew.types.date

        out["LastModifiedDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    out["Name"] = value["name"]
    if "recipe_name" in value:
        out["RecipeName"] = value["recipe_name"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "sample" in value:
        import aws_sdk_databrew.types.sample

        out["Sample"] = aws_sdk_databrew.types.sample.serialize_json(value["sample"])
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_databrew.types.tag_map

        out["Tags"] = aws_sdk_databrew.types.tag_map.serialize_json(value["tags"])
    if "session_status" in value:
        import aws_sdk_databrew.types.session_status

        out["SessionStatus"] = aws_sdk_databrew.types.session_status.serialize_json(
            value["session_status"]
        )
    if "opened_by" in value:
        out["OpenedBy"] = value["opened_by"]
    if "open_date" in value:
        import aws_sdk_databrew.types.date

        out["OpenDate"] = aws_sdk_databrew.types.date.serialize_json(value["open_date"])
    return out


def deserialize_json(data: dict) -> DescribeProjectResponse:
    out: DescribeProjectResponse = {}  # type: ignore[typeddict-item]
    if "CreateDate" in data:
        import aws_sdk_databrew.types.date

        out["create_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    if "LastModifiedDate" in data:
        import aws_sdk_databrew.types.date

        out["last_modified_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DescribeProjectResponse.name required")
    if "RecipeName" in data:
        out["recipe_name"] = data["RecipeName"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Sample" in data:
        import aws_sdk_databrew.types.sample

        out["sample"] = aws_sdk_databrew.types.sample.deserialize_json(data["Sample"])
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Tags" in data:
        import aws_sdk_databrew.types.tag_map

        out["tags"] = aws_sdk_databrew.types.tag_map.deserialize_json(data["Tags"])
    if "SessionStatus" in data:
        import aws_sdk_databrew.types.session_status

        out["session_status"] = aws_sdk_databrew.types.session_status.deserialize_json(
            data["SessionStatus"]
        )
    if "OpenedBy" in data:
        out["opened_by"] = data["OpenedBy"]
    if "OpenDate" in data:
        import aws_sdk_databrew.types.date

        out["open_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["OpenDate"]
        )
    return out
