"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeRecipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.arn
    import aws_sdk_databrew.types.created_by
    import aws_sdk_databrew.types.date
    import aws_sdk_databrew.types.last_modified_by
    import aws_sdk_databrew.types.project_name
    import aws_sdk_databrew.types.published_by
    import aws_sdk_databrew.types.recipe_description
    import aws_sdk_databrew.types.recipe_name
    import aws_sdk_databrew.types.recipe_step_list
    import aws_sdk_databrew.types.recipe_version
    import aws_sdk_databrew.types.tag_map


class DescribeRecipeResponse(TypedDict, closed=True):
    created_by: NotRequired["aws_sdk_databrew.types.created_by.CreatedBy"]
    """<p>The identifier (user name) of the user who created the recipe.</p>"""
    create_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the recipe was created.</p>"""
    last_modified_by: NotRequired[
        "aws_sdk_databrew.types.last_modified_by.LastModifiedBy"
    ]
    """<p>The identifier (user name) of the user who last modified the recipe.</p>"""
    last_modified_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the recipe was last modified.</p>"""
    project_name: NotRequired["aws_sdk_databrew.types.project_name.ProjectName"]
    """<p>The name of the project associated with this recipe.</p>"""
    published_by: NotRequired["aws_sdk_databrew.types.published_by.PublishedBy"]
    """<p>The identifier (user name) of the user who last published the recipe.</p>"""
    published_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time when the recipe was last published.</p>"""
    description: NotRequired[
        "aws_sdk_databrew.types.recipe_description.RecipeDescription"
    ]
    """<p>The description of the recipe.</p>"""
    name: "aws_sdk_databrew.types.recipe_name.RecipeName"
    """<p>The name of the recipe.</p>"""
    steps: NotRequired["aws_sdk_databrew.types.recipe_step_list.RecipeStepList"]
    """<p>One or more steps to be performed by the recipe. Each step consists of an action, and the conditions under which the action should succeed.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags associated with this project.</p>"""
    resource_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The ARN of the recipe.</p>"""
    recipe_version: NotRequired["aws_sdk_databrew.types.recipe_version.RecipeVersion"]
    """<p>The recipe version identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecipeResponse) -> dict:
    out: dict = {}
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "create_date" in value:
        import aws_sdk_databrew.types.date

        out["CreateDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["create_date"]
        )
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_date" in value:
        import aws_sdk_databrew.types.date

        out["LastModifiedDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    if "project_name" in value:
        out["ProjectName"] = value["project_name"]
    if "published_by" in value:
        out["PublishedBy"] = value["published_by"]
    if "published_date" in value:
        import aws_sdk_databrew.types.date

        out["PublishedDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["published_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    out["Name"] = value["name"]
    if "steps" in value:
        import aws_sdk_databrew.types.recipe_step_list

        out["Steps"] = aws_sdk_databrew.types.recipe_step_list.serialize_json(
            value["steps"]
        )
    if "tags" in value:
        import aws_sdk_databrew.types.tag_map

        out["Tags"] = aws_sdk_databrew.types.tag_map.serialize_json(value["tags"])
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "recipe_version" in value:
        out["RecipeVersion"] = value["recipe_version"]
    return out


def deserialize_json(data: dict) -> DescribeRecipeResponse:
    out: DescribeRecipeResponse = {}  # type: ignore[typeddict-item]
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "CreateDate" in data:
        import aws_sdk_databrew.types.date

        out["create_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    if "LastModifiedDate" in data:
        import aws_sdk_databrew.types.date

        out["last_modified_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if "ProjectName" in data:
        out["project_name"] = data["ProjectName"]
    if "PublishedBy" in data:
        out["published_by"] = data["PublishedBy"]
    if "PublishedDate" in data:
        import aws_sdk_databrew.types.date

        out["published_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["PublishedDate"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DescribeRecipeResponse.name required")
    if "Steps" in data:
        import aws_sdk_databrew.types.recipe_step_list

        out["steps"] = aws_sdk_databrew.types.recipe_step_list.deserialize_json(
            data["Steps"]
        )
    if "Tags" in data:
        import aws_sdk_databrew.types.tag_map

        out["tags"] = aws_sdk_databrew.types.tag_map.deserialize_json(data["Tags"])
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "RecipeVersion" in data:
        out["recipe_version"] = data["RecipeVersion"]
    return out
