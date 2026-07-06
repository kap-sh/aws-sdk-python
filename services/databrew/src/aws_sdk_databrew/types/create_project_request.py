"""Generated from Smithy shape ``com.amazonaws.databrew#CreateProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.arn
    import aws_sdk_databrew.types.dataset_name
    import aws_sdk_databrew.types.project_name
    import aws_sdk_databrew.types.recipe_name
    import aws_sdk_databrew.types.sample
    import aws_sdk_databrew.types.tag_map


class CreateProjectRequest(TypedDict, closed=True):
    dataset_name: "aws_sdk_databrew.types.dataset_name.DatasetName"
    """<p>The name of an existing dataset to associate this project with.</p>"""
    name: "aws_sdk_databrew.types.project_name.ProjectName"
    """<p>A unique name for the new project. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>"""
    recipe_name: "aws_sdk_databrew.types.recipe_name.RecipeName"
    """<p>The name of an existing recipe to associate with the project.</p>"""
    sample: NotRequired["aws_sdk_databrew.types.sample.Sample"]
    role_arn: "aws_sdk_databrew.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role to be assumed for this request.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags to apply to this project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectRequest) -> dict:
    out: dict = {}
    out["DatasetName"] = value["dataset_name"]
    out["Name"] = value["name"]
    out["RecipeName"] = value["recipe_name"]
    if "sample" in value:
        import aws_sdk_databrew.types.sample

        out["Sample"] = aws_sdk_databrew.types.sample.serialize_json(value["sample"])
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_databrew.types.tag_map

        out["Tags"] = aws_sdk_databrew.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateProjectRequest:
    out: CreateProjectRequest = {}  # type: ignore[typeddict-item]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    else:
        raise DeserializationError("CreateProjectRequest.dataset_name required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateProjectRequest.name required")
    if "RecipeName" in data:
        out["recipe_name"] = data["RecipeName"]
    else:
        raise DeserializationError("CreateProjectRequest.recipe_name required")
    if "Sample" in data:
        import aws_sdk_databrew.types.sample

        out["sample"] = aws_sdk_databrew.types.sample.deserialize_json(data["Sample"])
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("CreateProjectRequest.role_arn required")
    if "Tags" in data:
        import aws_sdk_databrew.types.tag_map

        out["tags"] = aws_sdk_databrew.types.tag_map.deserialize_json(data["Tags"])
    return out
