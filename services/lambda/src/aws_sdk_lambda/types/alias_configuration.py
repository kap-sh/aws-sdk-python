"""Generated from Smithy shape ``com.amazonaws.lambda#AliasConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.alias
    import aws_sdk_lambda.types.alias_routing_configuration
    import aws_sdk_lambda.types.description
    import aws_sdk_lambda.types.function_arn
    import aws_sdk_lambda.types.string
    import aws_sdk_lambda.types.version


class AliasConfiguration(TypedDict):
    alias_arn: NotRequired["aws_sdk_lambda.types.function_arn.FunctionArn"]
    """<p>The Amazon Resource Name (ARN) of the alias.</p>"""
    name: NotRequired["aws_sdk_lambda.types.alias.Alias"]
    """<p>The name of the alias.</p>"""
    function_version: NotRequired["aws_sdk_lambda.types.version.Version"]
    """<p>The function version that the alias invokes.</p>"""
    description: NotRequired["aws_sdk_lambda.types.description.Description"]
    """<p>A description of the alias.</p>"""
    routing_config: NotRequired[
        "aws_sdk_lambda.types.alias_routing_configuration.AliasRoutingConfiguration"
    ]
    """<p>The <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html\">routing configuration</a> of the alias.</p>"""
    revision_id: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>A unique identifier that changes when you update the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AliasConfiguration) -> dict:
    out: dict = {}
    if "alias_arn" in value:
        out["AliasArn"] = value["alias_arn"]
    if "name" in value:
        out["Name"] = value["name"]
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


def deserialize_json(data: dict) -> AliasConfiguration:
    out: AliasConfiguration = {}  # type: ignore[typeddict-item]
    if "AliasArn" in data:
        out["alias_arn"] = data["AliasArn"]
    if "Name" in data:
        out["name"] = data["Name"]
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
