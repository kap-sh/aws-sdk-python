"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateDataAccessorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_configuration_list
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.client_token
    import aws_sdk_qbusiness.types.data_accessor_authentication_detail
    import aws_sdk_qbusiness.types.data_accessor_name
    import aws_sdk_qbusiness.types.principal_role_arn
    import aws_sdk_qbusiness.types.tags


class CreateDataAccessorRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application.</p>"""
    principal: "aws_sdk_qbusiness.types.principal_role_arn.PrincipalRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role for the ISV that will be accessing the data.</p>"""
    action_configurations: (
        "aws_sdk_qbusiness.types.action_configuration_list.ActionConfigurationList"
    )
    """<p>A list of action configurations specifying the allowed actions and any associated filters.</p>"""
    client_token: NotRequired["aws_sdk_qbusiness.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier you provide to ensure idempotency of the request.</p>"""
    display_name: "aws_sdk_qbusiness.types.data_accessor_name.DataAccessorName"
    """<p>A friendly name for the data accessor.</p>"""
    authentication_detail: NotRequired[
        "aws_sdk_qbusiness.types.data_accessor_authentication_detail.DataAccessorAuthenticationDetail"
    ]
    """<p>The authentication configuration details for the data accessor. This specifies how the ISV will authenticate when accessing data through this data accessor.</p>"""
    tags: NotRequired["aws_sdk_qbusiness.types.tags.Tags"]
    """<p>The tags to associate with the data accessor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataAccessorRequest) -> dict:
    out: dict = {}
    out["principal"] = value["principal"]
    import aws_sdk_qbusiness.types.action_configuration_list

    out["actionConfigurations"] = (
        aws_sdk_qbusiness.types.action_configuration_list.serialize_json(
            value["action_configurations"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["displayName"] = value["display_name"]
    if "authentication_detail" in value:
        import aws_sdk_qbusiness.types.data_accessor_authentication_detail

        out["authenticationDetail"] = (
            aws_sdk_qbusiness.types.data_accessor_authentication_detail.serialize_json(
                value["authentication_detail"]
            )
        )
    if "tags" in value:
        import aws_sdk_qbusiness.types.tags

        out["tags"] = aws_sdk_qbusiness.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDataAccessorRequest:
    out: CreateDataAccessorRequest = {}  # type: ignore[typeddict-item]
    if "principal" in data:
        out["principal"] = data["principal"]
    else:
        raise DeserializationError("CreateDataAccessorRequest.principal required")
    if "actionConfigurations" in data:
        import aws_sdk_qbusiness.types.action_configuration_list

        out["action_configurations"] = (
            aws_sdk_qbusiness.types.action_configuration_list.deserialize_json(
                data["actionConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataAccessorRequest.action_configurations required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateDataAccessorRequest.display_name required")
    if "authenticationDetail" in data:
        import aws_sdk_qbusiness.types.data_accessor_authentication_detail

        out["authentication_detail"] = (
            aws_sdk_qbusiness.types.data_accessor_authentication_detail.deserialize_json(
                data["authenticationDetail"]
            )
        )
    if "tags" in data:
        import aws_sdk_qbusiness.types.tags

        out["tags"] = aws_sdk_qbusiness.types.tags.deserialize_json(data["tags"])
    return out
