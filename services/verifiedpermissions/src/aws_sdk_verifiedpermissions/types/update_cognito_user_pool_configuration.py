"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdateCognitoUserPoolConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.client_ids
    import aws_sdk_verifiedpermissions.types.update_cognito_group_configuration
    import aws_sdk_verifiedpermissions.types.user_pool_arn


class UpdateCognitoUserPoolConfiguration(TypedDict, closed=True):
    user_pool_arn: "aws_sdk_verifiedpermissions.types.user_pool_arn.UserPoolArn"
    r"""<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the Amazon Cognito user pool associated with this identity source.</p>"""
    client_ids: NotRequired["aws_sdk_verifiedpermissions.types.client_ids.ClientIds"]
    """<p>The client ID of an app client that is configured for the specified Amazon Cognito user pool.</p>"""
    group_configuration: NotRequired[
        "aws_sdk_verifiedpermissions.types.update_cognito_group_configuration.UpdateCognitoGroupConfiguration"
    ]
    """<p>The configuration of the user groups from an Amazon Cognito user pool identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCognitoUserPoolConfiguration) -> dict:
    out: dict = {}
    out["userPoolArn"] = value["user_pool_arn"]
    if "client_ids" in value:
        import aws_sdk_verifiedpermissions.types.client_ids

        out["clientIds"] = (
            aws_sdk_verifiedpermissions.types.client_ids.serialize_aws_json_1_0(
                value["client_ids"]
            )
        )
    if "group_configuration" in value:
        import aws_sdk_verifiedpermissions.types.update_cognito_group_configuration

        out["groupConfiguration"] = (
            aws_sdk_verifiedpermissions.types.update_cognito_group_configuration.serialize_aws_json_1_0(
                value["group_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCognitoUserPoolConfiguration:
    out: UpdateCognitoUserPoolConfiguration = {}  # type: ignore[typeddict-item]
    if "userPoolArn" in data:
        out["user_pool_arn"] = data["userPoolArn"]
    else:
        raise DeserializationError(
            "UpdateCognitoUserPoolConfiguration.user_pool_arn required"
        )
    if "clientIds" in data:
        import aws_sdk_verifiedpermissions.types.client_ids

        out["client_ids"] = (
            aws_sdk_verifiedpermissions.types.client_ids.deserialize_aws_json_1_0(
                data["clientIds"]
            )
        )
    if "groupConfiguration" in data:
        import aws_sdk_verifiedpermissions.types.update_cognito_group_configuration

        out["group_configuration"] = (
            aws_sdk_verifiedpermissions.types.update_cognito_group_configuration.deserialize_aws_json_1_0(
                data["groupConfiguration"]
            )
        )
    return out
