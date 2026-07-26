"""Generated from Smithy shape ``com.amazonaws.sagemaker#MemberDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cognito_member_definition
    import capo_sagemaker.types.oidc_member_definition


class MemberDefinition(TypedDict, closed=True):
    cognito_member_definition: NotRequired[
        "capo_sagemaker.types.cognito_member_definition.CognitoMemberDefinition"
    ]
    """<p>The Amazon Cognito user group that is part of the work team.</p>"""
    oidc_member_definition: NotRequired[
        "capo_sagemaker.types.oidc_member_definition.OidcMemberDefinition"
    ]
    """<p>A list user groups that exist in your OIDC Identity Provider (IdP). One to ten groups can be used to create a single private work team. When you add a user group to the list of <code>Groups</code>, you can add that user group to one or more private work teams. If you add a user group to a private work team, all workers in that user group are added to the work team.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberDefinition) -> dict:
    out: dict = {}
    if "cognito_member_definition" in value:
        import capo_sagemaker.types.cognito_member_definition

        out["CognitoMemberDefinition"] = (
            capo_sagemaker.types.cognito_member_definition.serialize_aws_json_1_1(
                value["cognito_member_definition"]
            )
        )
    if "oidc_member_definition" in value:
        import capo_sagemaker.types.oidc_member_definition

        out["OidcMemberDefinition"] = (
            capo_sagemaker.types.oidc_member_definition.serialize_aws_json_1_1(
                value["oidc_member_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MemberDefinition:
    out: MemberDefinition = {}  # type: ignore[typeddict-item]
    if "CognitoMemberDefinition" in data:
        import capo_sagemaker.types.cognito_member_definition

        out["cognito_member_definition"] = (
            capo_sagemaker.types.cognito_member_definition.deserialize_aws_json_1_1(
                data["CognitoMemberDefinition"]
            )
        )
    if "OidcMemberDefinition" in data:
        import capo_sagemaker.types.oidc_member_definition

        out["oidc_member_definition"] = (
            capo_sagemaker.types.oidc_member_definition.deserialize_aws_json_1_1(
                data["OidcMemberDefinition"]
            )
        )
    return out
