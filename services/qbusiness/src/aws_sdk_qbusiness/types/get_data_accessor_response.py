"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetDataAccessorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_configuration_list
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.data_accessor_arn
    import aws_sdk_qbusiness.types.data_accessor_authentication_detail
    import aws_sdk_qbusiness.types.data_accessor_id
    import aws_sdk_qbusiness.types.data_accessor_name
    import aws_sdk_qbusiness.types.idc_application_arn
    import aws_sdk_qbusiness.types.principal_role_arn
    import aws_sdk_qbusiness.types.timestamp


class GetDataAccessorResponse(TypedDict, closed=True):
    display_name: NotRequired[
        "aws_sdk_qbusiness.types.data_accessor_name.DataAccessorName"
    ]
    """<p>The friendly name of the data accessor.</p>"""
    data_accessor_id: NotRequired[
        "aws_sdk_qbusiness.types.data_accessor_id.DataAccessorId"
    ]
    """<p>The unique identifier of the data accessor.</p>"""
    data_accessor_arn: NotRequired[
        "aws_sdk_qbusiness.types.data_accessor_arn.DataAccessorArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the data accessor.</p>"""
    application_id: NotRequired["aws_sdk_qbusiness.types.application_id.ApplicationId"]
    """<p>The unique identifier of the Amazon Q Business application associated with this data accessor.</p>"""
    idc_application_arn: NotRequired[
        "aws_sdk_qbusiness.types.idc_application_arn.IdcApplicationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center application associated with this data accessor.</p>"""
    principal: NotRequired[
        "aws_sdk_qbusiness.types.principal_role_arn.PrincipalRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role for the ISV associated with this data accessor.</p>"""
    action_configurations: NotRequired[
        "aws_sdk_qbusiness.types.action_configuration_list.ActionConfigurationList"
    ]
    """<p>The list of action configurations specifying the allowed actions and any associated filters.</p>"""
    authentication_detail: NotRequired[
        "aws_sdk_qbusiness.types.data_accessor_authentication_detail.DataAccessorAuthenticationDetail"
    ]
    """<p>The authentication configuration details for the data accessor. This specifies how the ISV authenticates when accessing data through this data accessor.</p>"""
    created_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp when the data accessor was created.</p>"""
    updated_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp when the data accessor was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataAccessorResponse) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "data_accessor_id" in value:
        out["dataAccessorId"] = value["data_accessor_id"]
    if "data_accessor_arn" in value:
        out["dataAccessorArn"] = value["data_accessor_arn"]
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "idc_application_arn" in value:
        out["idcApplicationArn"] = value["idc_application_arn"]
    if "principal" in value:
        out["principal"] = value["principal"]
    if "action_configurations" in value:
        import aws_sdk_qbusiness.types.action_configuration_list

        out["actionConfigurations"] = (
            aws_sdk_qbusiness.types.action_configuration_list.serialize_json(
                value["action_configurations"]
            )
        )
    if "authentication_detail" in value:
        import aws_sdk_qbusiness.types.data_accessor_authentication_detail

        out["authenticationDetail"] = (
            aws_sdk_qbusiness.types.data_accessor_authentication_detail.serialize_json(
                value["authentication_detail"]
            )
        )
    if "created_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["createdAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["updatedAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetDataAccessorResponse:
    out: GetDataAccessorResponse = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "dataAccessorId" in data:
        out["data_accessor_id"] = data["dataAccessorId"]
    if "dataAccessorArn" in data:
        out["data_accessor_arn"] = data["dataAccessorArn"]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "idcApplicationArn" in data:
        out["idc_application_arn"] = data["idcApplicationArn"]
    if "principal" in data:
        out["principal"] = data["principal"]
    if "actionConfigurations" in data:
        import aws_sdk_qbusiness.types.action_configuration_list

        out["action_configurations"] = (
            aws_sdk_qbusiness.types.action_configuration_list.deserialize_json(
                data["actionConfigurations"]
            )
        )
    if "authenticationDetail" in data:
        import aws_sdk_qbusiness.types.data_accessor_authentication_detail

        out["authentication_detail"] = (
            aws_sdk_qbusiness.types.data_accessor_authentication_detail.deserialize_json(
                data["authenticationDetail"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["created_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["updated_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
