"""Generated from Smithy shape ``com.amazonaws.personalize#CreateFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.filter_expression
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.tags


class CreateFilterRequest(TypedDict, closed=True):
    name: "aws_sdk_personalize.types.name.Name"
    """<p>The name of the filter to create.</p>"""
    dataset_group_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The ARN of the dataset group that the filter will belong to.</p>"""
    filter_expression: "aws_sdk_personalize.types.filter_expression.FilterExpression"
    r"""<p>The filter expression defines which items are included or excluded from recommendations. Filter expression must follow specific format rules. For information about filter expression structure and syntax, see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/filter-expressions.html\">Filter expressions</a>.</p>"""
    tags: NotRequired["aws_sdk_personalize.types.tags.Tags"]
    r"""<p>A list of <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html\">tags</a> to apply to the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFilterRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["datasetGroupArn"] = value["dataset_group_arn"]
    out["filterExpression"] = value["filter_expression"]
    if "tags" in value:
        import aws_sdk_personalize.types.tags

        out["tags"] = aws_sdk_personalize.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFilterRequest:
    out: CreateFilterRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFilterRequest.name required")
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    else:
        raise DeserializationError("CreateFilterRequest.dataset_group_arn required")
    if "filterExpression" in data:
        out["filter_expression"] = data["filterExpression"]
    else:
        raise DeserializationError("CreateFilterRequest.filter_expression required")
    if "tags" in data:
        import aws_sdk_personalize.types.tags

        out["tags"] = aws_sdk_personalize.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
