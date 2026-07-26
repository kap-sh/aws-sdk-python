"""Generated from Smithy shape ``com.amazonaws.codedeploy#LambdaFunctionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.lambda_function_alias
    import capo_codedeploy.types.lambda_function_name
    import capo_codedeploy.types.traffic_weight
    import capo_codedeploy.types.version


class LambdaFunctionInfo(TypedDict, closed=True):
    function_name: NotRequired[
        "capo_codedeploy.types.lambda_function_name.LambdaFunctionName"
    ]
    """<p> The name of a Lambda function. </p>"""
    function_alias: NotRequired[
        "capo_codedeploy.types.lambda_function_alias.LambdaFunctionAlias"
    ]
    r"""<p> The alias of a Lambda function. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html\">Lambda Function Aliases</a> in the <i>Lambda Developer Guide</i>.</p>"""
    current_version: NotRequired["capo_codedeploy.types.version.Version"]
    """<p> The version of a Lambda function that production traffic points to. </p>"""
    target_version: NotRequired["capo_codedeploy.types.version.Version"]
    """<p> The version of a Lambda function that production traffic points to after the Lambda function is deployed. </p>"""
    target_version_weight: "capo_codedeploy.types.traffic_weight.TrafficWeight"
    """<p> The percentage of production traffic that the target version of a Lambda function receives. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaFunctionInfo) -> dict:
    out: dict = {}
    if "function_name" in value:
        out["functionName"] = value["function_name"]
    if "function_alias" in value:
        out["functionAlias"] = value["function_alias"]
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "target_version" in value:
        out["targetVersion"] = value["target_version"]
    out["targetVersionWeight"] = value.get("target_version_weight", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> LambdaFunctionInfo:
    out: LambdaFunctionInfo = {}  # type: ignore[typeddict-item]
    if "functionName" in data:
        out["function_name"] = data["functionName"]
    if "functionAlias" in data:
        out["function_alias"] = data["functionAlias"]
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "targetVersion" in data:
        out["target_version"] = data["targetVersion"]
    if "targetVersionWeight" in data:
        out["target_version_weight"] = data["targetVersionWeight"]
    else:
        out["target_version_weight"] = 0
    return out
