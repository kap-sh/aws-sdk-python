"""Generated from Smithy shape ``com.amazonaws.lambda#UpdateAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.alias
    import aws_sdk_lambda.types.alias_routing_configuration
    import aws_sdk_lambda.types.description
    import aws_sdk_lambda.types.function_name
    import aws_sdk_lambda.types.string
    import aws_sdk_lambda.types.version_with_latest_published


class UpdateAliasRequest(TypedDict):
    function_name: "aws_sdk_lambda.types.function_name.FunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    name: "aws_sdk_lambda.types.alias.Alias"
    """<p>The name of the alias.</p>"""
    function_version: NotRequired[
        "aws_sdk_lambda.types.version_with_latest_published.VersionWithLatestPublished"
    ]
    """<p>The function version that the alias invokes.</p>"""
    description: NotRequired["aws_sdk_lambda.types.description.Description"]
    """<p>A description of the alias.</p>"""
    routing_config: NotRequired[
        "aws_sdk_lambda.types.alias_routing_configuration.AliasRoutingConfiguration"
    ]
    """<p>The <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html#configuring-alias-routing\">routing configuration</a> of the alias.</p>"""
    revision_id: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>Only update the alias if the revision ID matches the ID that's specified. Use this option to avoid modifying an alias that has changed since you last read it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAliasRequest) -> dict:
    out: dict = {}
    if "function_version" in value:
        out["FunctionVersion"] = value["function_version"]
    if "description" in value:
        out["Description"] = value["description"]
    if "routing_config" in value:
        import aws_sdk_lambda.types.alias_routing_configuration

        out["RoutingConfig"] = (
            aws_sdk_lambda.types.alias_routing_configuration.serialize_json(
                value["routing_config"]
            )
        )
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> UpdateAliasRequest:
    out: UpdateAliasRequest = {}  # type: ignore[typeddict-item]
    if "FunctionVersion" in data:
        out["function_version"] = data["FunctionVersion"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoutingConfig" in data:
        import aws_sdk_lambda.types.alias_routing_configuration

        out["routing_config"] = (
            aws_sdk_lambda.types.alias_routing_configuration.deserialize_json(
                data["RoutingConfig"]
            )
        )
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    return out
