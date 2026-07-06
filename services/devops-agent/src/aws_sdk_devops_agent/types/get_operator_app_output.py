"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetOperatorAppOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.iam_auth_configuration
    import aws_sdk_devops_agent.types.idc_auth_configuration
    import aws_sdk_devops_agent.types.idp_auth_configuration
    import aws_sdk_devops_agent.types.operator_app_url


class GetOperatorAppOutput(TypedDict, closed=True):
    operator_app_url: NotRequired[
        "aws_sdk_devops_agent.types.operator_app_url.OperatorAppUrl"
    ]
    """<p>The URL for operators to access the Operator App</p>"""
    iam: NotRequired[
        "aws_sdk_devops_agent.types.iam_auth_configuration.IamAuthConfiguration"
    ]
    idc: NotRequired[
        "aws_sdk_devops_agent.types.idc_auth_configuration.IdcAuthConfiguration"
    ]
    idp: NotRequired[
        "aws_sdk_devops_agent.types.idp_auth_configuration.IdpAuthConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetOperatorAppOutput) -> dict:
    out: dict = {}
    if "operator_app_url" in value:
        out["operatorAppUrl"] = value["operator_app_url"]
    if "iam" in value:
        import aws_sdk_devops_agent.types.iam_auth_configuration

        out["iam"] = aws_sdk_devops_agent.types.iam_auth_configuration.serialize_json(
            value["iam"]
        )
    if "idc" in value:
        import aws_sdk_devops_agent.types.idc_auth_configuration

        out["idc"] = aws_sdk_devops_agent.types.idc_auth_configuration.serialize_json(
            value["idc"]
        )
    if "idp" in value:
        import aws_sdk_devops_agent.types.idp_auth_configuration

        out["idp"] = aws_sdk_devops_agent.types.idp_auth_configuration.serialize_json(
            value["idp"]
        )
    return out


def deserialize_json(data: dict) -> GetOperatorAppOutput:
    out: GetOperatorAppOutput = {}  # type: ignore[typeddict-item]
    if "operatorAppUrl" in data:
        out["operator_app_url"] = data["operatorAppUrl"]
    if "iam" in data:
        import aws_sdk_devops_agent.types.iam_auth_configuration

        out["iam"] = aws_sdk_devops_agent.types.iam_auth_configuration.deserialize_json(
            data["iam"]
        )
    if "idc" in data:
        import aws_sdk_devops_agent.types.idc_auth_configuration

        out["idc"] = aws_sdk_devops_agent.types.idc_auth_configuration.deserialize_json(
            data["idc"]
        )
    if "idp" in data:
        import aws_sdk_devops_agent.types.idp_auth_configuration

        out["idp"] = aws_sdk_devops_agent.types.idp_auth_configuration.deserialize_json(
            data["idp"]
        )
    return out
