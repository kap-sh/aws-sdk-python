"""Generated from Smithy shape ``com.amazonaws.budgets#Definition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_budgets.types.iam_action_definition
    import aws_sdk_budgets.types.scp_action_definition
    import aws_sdk_budgets.types.ssm_action_definition


class Definition(TypedDict):
    iam_action_definition: NotRequired[
        "aws_sdk_budgets.types.iam_action_definition.IamActionDefinition"
    ]
    """<p>The Identity and Access Management (IAM) action definition details. </p>"""
    scp_action_definition: NotRequired[
        "aws_sdk_budgets.types.scp_action_definition.ScpActionDefinition"
    ]
    """<p>The service control policies (SCPs) action definition details. </p>"""
    ssm_action_definition: NotRequired[
        "aws_sdk_budgets.types.ssm_action_definition.SsmActionDefinition"
    ]
    """<p>The Amazon Web Services Systems Manager (SSM) action definition details. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Definition) -> dict:
    out: dict = {}
    if "iam_action_definition" in value:
        import aws_sdk_budgets.types.iam_action_definition

        out["IamActionDefinition"] = (
            aws_sdk_budgets.types.iam_action_definition.serialize_aws_json_1_1(
                value["iam_action_definition"]
            )
        )
    if "scp_action_definition" in value:
        import aws_sdk_budgets.types.scp_action_definition

        out["ScpActionDefinition"] = (
            aws_sdk_budgets.types.scp_action_definition.serialize_aws_json_1_1(
                value["scp_action_definition"]
            )
        )
    if "ssm_action_definition" in value:
        import aws_sdk_budgets.types.ssm_action_definition

        out["SsmActionDefinition"] = (
            aws_sdk_budgets.types.ssm_action_definition.serialize_aws_json_1_1(
                value["ssm_action_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Definition:
    out: Definition = {}  # type: ignore[typeddict-item]
    if "IamActionDefinition" in data:
        import aws_sdk_budgets.types.iam_action_definition

        out["iam_action_definition"] = (
            aws_sdk_budgets.types.iam_action_definition.deserialize_aws_json_1_1(
                data["IamActionDefinition"]
            )
        )
    if "ScpActionDefinition" in data:
        import aws_sdk_budgets.types.scp_action_definition

        out["scp_action_definition"] = (
            aws_sdk_budgets.types.scp_action_definition.deserialize_aws_json_1_1(
                data["ScpActionDefinition"]
            )
        )
    if "SsmActionDefinition" in data:
        import aws_sdk_budgets.types.ssm_action_definition

        out["ssm_action_definition"] = (
            aws_sdk_budgets.types.ssm_action_definition.deserialize_aws_json_1_1(
                data["SsmActionDefinition"]
            )
        )
    return out
