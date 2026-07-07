"""Generated from Smithy shape ``com.amazonaws.glue#StartBlueprintRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.blueprint_parameters
    import aws_sdk_glue.types.orchestration_iam_role_arn
    import aws_sdk_glue.types.orchestration_name_string


class StartBlueprintRunRequest(TypedDict, closed=True):
    blueprint_name: (
        "aws_sdk_glue.types.orchestration_name_string.OrchestrationNameString"
    )
    """<p>The name of the blueprint.</p>"""
    parameters: NotRequired[
        "aws_sdk_glue.types.blueprint_parameters.BlueprintParameters"
    ]
    """<p>Specifies the parameters as a <code>BlueprintParameters</code> object.</p>"""
    role_arn: "aws_sdk_glue.types.orchestration_iam_role_arn.OrchestrationIAMRoleArn"
    """<p>Specifies the IAM role used to create the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartBlueprintRunRequest) -> dict:
    out: dict = {}
    out["BlueprintName"] = value["blueprint_name"]
    if "parameters" in value:
        out["Parameters"] = value["parameters"]
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartBlueprintRunRequest:
    out: StartBlueprintRunRequest = {}  # type: ignore[typeddict-item]
    if "BlueprintName" in data:
        out["blueprint_name"] = data["BlueprintName"]
    else:
        raise DeserializationError("StartBlueprintRunRequest.blueprint_name required")
    if "Parameters" in data:
        out["parameters"] = data["Parameters"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("StartBlueprintRunRequest.role_arn required")
    return out
