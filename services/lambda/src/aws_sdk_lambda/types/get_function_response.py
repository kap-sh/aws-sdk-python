"""Generated from Smithy shape ``com.amazonaws.lambda#GetFunctionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.concurrency
    import aws_sdk_lambda.types.function_code_location
    import aws_sdk_lambda.types.function_configuration
    import aws_sdk_lambda.types.tags
    import aws_sdk_lambda.types.tags_error


class GetFunctionResponse(TypedDict):
    configuration: NotRequired[
        "aws_sdk_lambda.types.function_configuration.FunctionConfiguration"
    ]
    """<p>The configuration of the function or version.</p>"""
    code: NotRequired[
        "aws_sdk_lambda.types.function_code_location.FunctionCodeLocation"
    ]
    """<p>The deployment package of the function or version.</p>"""
    tags: NotRequired["aws_sdk_lambda.types.tags.Tags"]
    r"""<p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a>. Lambda returns tag data only if you have explicit allow permissions for <a href=\"https://docs.aws.amazon.com/lambda/latest/api/API_ListTags.html\">lambda:ListTags</a>.</p>"""
    tags_error: NotRequired["aws_sdk_lambda.types.tags_error.TagsError"]
    """<p>An object that contains details about an error related to retrieving tags.</p>"""
    concurrency: NotRequired["aws_sdk_lambda.types.concurrency.Concurrency"]
    r"""<p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html\">reserved concurrency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionResponse) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_lambda.types.function_configuration

        out["Configuration"] = (
            aws_sdk_lambda.types.function_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "code" in value:
        import aws_sdk_lambda.types.function_code_location

        out["Code"] = aws_sdk_lambda.types.function_code_location.serialize_json(
            value["code"]
        )
    if "tags" in value:
        import aws_sdk_lambda.types.tags

        out["Tags"] = aws_sdk_lambda.types.tags.serialize_json(value["tags"])
    if "tags_error" in value:
        import aws_sdk_lambda.types.tags_error

        out["TagsError"] = aws_sdk_lambda.types.tags_error.serialize_json(
            value["tags_error"]
        )
    if "concurrency" in value:
        import aws_sdk_lambda.types.concurrency

        out["Concurrency"] = aws_sdk_lambda.types.concurrency.serialize_json(
            value["concurrency"]
        )
    return out


def deserialize_json(data: dict) -> GetFunctionResponse:
    out: GetFunctionResponse = {}  # type: ignore[typeddict-item]
    if "Configuration" in data:
        import aws_sdk_lambda.types.function_configuration

        out["configuration"] = (
            aws_sdk_lambda.types.function_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if "Code" in data:
        import aws_sdk_lambda.types.function_code_location

        out["code"] = aws_sdk_lambda.types.function_code_location.deserialize_json(
            data["Code"]
        )
    if "Tags" in data:
        import aws_sdk_lambda.types.tags

        out["tags"] = aws_sdk_lambda.types.tags.deserialize_json(data["Tags"])
    if "TagsError" in data:
        import aws_sdk_lambda.types.tags_error

        out["tags_error"] = aws_sdk_lambda.types.tags_error.deserialize_json(
            data["TagsError"]
        )
    if "Concurrency" in data:
        import aws_sdk_lambda.types.concurrency

        out["concurrency"] = aws_sdk_lambda.types.concurrency.deserialize_json(
            data["Concurrency"]
        )
    return out
