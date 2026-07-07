"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CognitoUserPoolConfigurationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.client_ids
    import aws_sdk_verifiedpermissions.types.cognito_group_configuration_detail
    import aws_sdk_verifiedpermissions.types.issuer
    import aws_sdk_verifiedpermissions.types.user_pool_arn


class CognitoUserPoolConfigurationDetail(TypedDict, closed=True):
    user_pool_arn: "aws_sdk_verifiedpermissions.types.user_pool_arn.UserPoolArn"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the Amazon Cognito user pool that contains the identities to be authorized.</p> <p>Example: <code>\"userPoolArn\": \"arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5\"</code> </p>"""
    client_ids: "aws_sdk_verifiedpermissions.types.client_ids.ClientIds"
    r"""<p>The unique application client IDs that are associated with the specified Amazon Cognito user pool.</p> <p>Example: <code>\"clientIds\": [\"&amp;ExampleCogClientId;\"]</code> </p>"""
    issuer: "aws_sdk_verifiedpermissions.types.issuer.Issuer"
    r"""<p>The OpenID Connect (OIDC) <code>issuer</code> ID of the Amazon Cognito user pool that contains the identities to be authorized.</p> <p>Example: <code>\"issuer\": \"https://cognito-idp.us-east-1.amazonaws.com/us-east-1_1a2b3c4d5\"</code> </p>"""
    group_configuration: NotRequired[
        "aws_sdk_verifiedpermissions.types.cognito_group_configuration_detail.CognitoGroupConfigurationDetail"
    ]
    """<p>The type of entity that a policy store maps to groups from an Amazon Cognito user pool identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CognitoUserPoolConfigurationDetail) -> dict:
    out: dict = {}
    out["userPoolArn"] = value["user_pool_arn"]
    import aws_sdk_verifiedpermissions.types.client_ids

    out["clientIds"] = (
        aws_sdk_verifiedpermissions.types.client_ids.serialize_aws_json_1_0(
            value["client_ids"]
        )
    )
    out["issuer"] = value["issuer"]
    if "group_configuration" in value:
        import aws_sdk_verifiedpermissions.types.cognito_group_configuration_detail

        out["groupConfiguration"] = (
            aws_sdk_verifiedpermissions.types.cognito_group_configuration_detail.serialize_aws_json_1_0(
                value["group_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CognitoUserPoolConfigurationDetail:
    out: CognitoUserPoolConfigurationDetail = {}  # type: ignore[typeddict-item]
    if "userPoolArn" in data:
        out["user_pool_arn"] = data["userPoolArn"]
    else:
        raise DeserializationError(
            "CognitoUserPoolConfigurationDetail.user_pool_arn required"
        )
    if "clientIds" in data:
        import aws_sdk_verifiedpermissions.types.client_ids

        out["client_ids"] = (
            aws_sdk_verifiedpermissions.types.client_ids.deserialize_aws_json_1_0(
                data["clientIds"]
            )
        )
    else:
        raise DeserializationError(
            "CognitoUserPoolConfigurationDetail.client_ids required"
        )
    if "issuer" in data:
        out["issuer"] = data["issuer"]
    else:
        raise DeserializationError("CognitoUserPoolConfigurationDetail.issuer required")
    if "groupConfiguration" in data:
        import aws_sdk_verifiedpermissions.types.cognito_group_configuration_detail

        out["group_configuration"] = (
            aws_sdk_verifiedpermissions.types.cognito_group_configuration_detail.deserialize_aws_json_1_0(
                data["groupConfiguration"]
            )
        )
    return out
