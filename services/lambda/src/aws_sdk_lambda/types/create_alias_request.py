"""Generated from Smithy shape ``com.amazonaws.lambda#CreateAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.alias
    import aws_sdk_lambda.types.alias_routing_configuration
    import aws_sdk_lambda.types.description
    import aws_sdk_lambda.types.function_name
    import aws_sdk_lambda.types.version_with_latest_published


class CreateAliasRequest(TypedDict, closed=True):
    function_name: "aws_sdk_lambda.types.function_name.FunctionName"
    r"""<p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    name: "aws_sdk_lambda.types.alias.Alias"
    """<p>The name of the alias.</p>"""
    function_version: (
        "aws_sdk_lambda.types.version_with_latest_published.VersionWithLatestPublished"
    )
    """<p>The function version that the alias invokes.</p>"""
    description: NotRequired["aws_sdk_lambda.types.description.Description"]
    """<p>A description of the alias.</p>"""
    routing_config: NotRequired[
        "aws_sdk_lambda.types.alias_routing_configuration.AliasRoutingConfiguration"
    ]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html#configuring-alias-routing\">routing configuration</a> of the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAliasRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
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
    return out


def deserialize_json(data: dict) -> CreateAliasRequest:
    out: CreateAliasRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateAliasRequest.name required")
    if "FunctionVersion" in data:
        out["function_version"] = data["FunctionVersion"]
    else:
        raise DeserializationError("CreateAliasRequest.function_version required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoutingConfig" in data:
        import aws_sdk_lambda.types.alias_routing_configuration

        out["routing_config"] = (
            aws_sdk_lambda.types.alias_routing_configuration.deserialize_json(
                data["RoutingConfig"]
            )
        )
    return out
