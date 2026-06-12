"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaFunctionRecipeSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.component_dependency_map
    import aws_sdk_greengrassv2.types.component_name_string
    import aws_sdk_greengrassv2.types.component_platform_list
    import aws_sdk_greengrassv2.types.component_version_string
    import aws_sdk_greengrassv2.types.lambda_execution_parameters
    import aws_sdk_greengrassv2.types.non_empty_string


class LambdaFunctionRecipeSource(TypedDict):
    lambda_arn: "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the Lambda function. The ARN must include the version of the function to import. You can't use version aliases like <code>$LATEST</code>.</p>"""
    component_name: NotRequired[
        "aws_sdk_greengrassv2.types.component_name_string.ComponentNameString"
    ]
    """<p>The name of the component.</p> <p>Defaults to the name of the Lambda function.</p>"""
    component_version: NotRequired[
        "aws_sdk_greengrassv2.types.component_version_string.ComponentVersionString"
    ]
    """<p>The version of the component.</p> <p>Defaults to the version of the Lambda function as a semantic version. For example, if your function version is <code>3</code>, the component version becomes <code>3.0.0</code>.</p>"""
    component_platforms: NotRequired[
        "aws_sdk_greengrassv2.types.component_platform_list.ComponentPlatformList"
    ]
    """<p>The platforms that the component version supports.</p>"""
    component_dependencies: NotRequired[
        "aws_sdk_greengrassv2.types.component_dependency_map.ComponentDependencyMap"
    ]
    """<p>The component versions on which this Lambda function component depends.</p>"""
    component_lambda_parameters: NotRequired[
        "aws_sdk_greengrassv2.types.lambda_execution_parameters.LambdaExecutionParameters"
    ]
    """<p>The system and runtime parameters for the Lambda function as it runs on the Greengrass core device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaFunctionRecipeSource) -> dict:
    out: dict = {}
    out["lambdaArn"] = value["lambda_arn"]
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_version" in value:
        out["componentVersion"] = value["component_version"]
    if "component_platforms" in value:
        import aws_sdk_greengrassv2.types.component_platform_list

        out["componentPlatforms"] = (
            aws_sdk_greengrassv2.types.component_platform_list.serialize_json(
                value["component_platforms"]
            )
        )
    if "component_dependencies" in value:
        import aws_sdk_greengrassv2.types.component_dependency_map

        out["componentDependencies"] = (
            aws_sdk_greengrassv2.types.component_dependency_map.serialize_json(
                value["component_dependencies"]
            )
        )
    if "component_lambda_parameters" in value:
        import aws_sdk_greengrassv2.types.lambda_execution_parameters

        out["componentLambdaParameters"] = (
            aws_sdk_greengrassv2.types.lambda_execution_parameters.serialize_json(
                value["component_lambda_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> LambdaFunctionRecipeSource:
    out: LambdaFunctionRecipeSource = {}  # type: ignore[typeddict-item]
    if "lambdaArn" in data:
        out["lambda_arn"] = data["lambdaArn"]
    else:
        raise DeserializationError("LambdaFunctionRecipeSource.lambda_arn required")
    if "componentName" in data:
        out["component_name"] = data["componentName"]
    if "componentVersion" in data:
        out["component_version"] = data["componentVersion"]
    if "componentPlatforms" in data:
        import aws_sdk_greengrassv2.types.component_platform_list

        out["component_platforms"] = (
            aws_sdk_greengrassv2.types.component_platform_list.deserialize_json(
                data["componentPlatforms"]
            )
        )
    if "componentDependencies" in data:
        import aws_sdk_greengrassv2.types.component_dependency_map

        out["component_dependencies"] = (
            aws_sdk_greengrassv2.types.component_dependency_map.deserialize_json(
                data["componentDependencies"]
            )
        )
    if "componentLambdaParameters" in data:
        import aws_sdk_greengrassv2.types.lambda_execution_parameters

        out["component_lambda_parameters"] = (
            aws_sdk_greengrassv2.types.lambda_execution_parameters.deserialize_json(
                data["componentLambdaParameters"]
            )
        )
    return out
