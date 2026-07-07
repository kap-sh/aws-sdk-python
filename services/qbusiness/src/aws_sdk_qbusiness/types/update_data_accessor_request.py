"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateDataAccessorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_configuration_list
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.data_accessor_authentication_detail
    import aws_sdk_qbusiness.types.data_accessor_id
    import aws_sdk_qbusiness.types.data_accessor_name


class UpdateDataAccessorRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application.</p>"""
    data_accessor_id: "aws_sdk_qbusiness.types.data_accessor_id.DataAccessorId"
    """<p>The unique identifier of the data accessor to update.</p>"""
    action_configurations: (
        "aws_sdk_qbusiness.types.action_configuration_list.ActionConfigurationList"
    )
    """<p>The updated list of action configurations specifying the allowed actions and any associated filters.</p>"""
    authentication_detail: NotRequired[
        "aws_sdk_qbusiness.types.data_accessor_authentication_detail.DataAccessorAuthenticationDetail"
    ]
    """<p>The updated authentication configuration details for the data accessor. This specifies how the ISV will authenticate when accessing data through this data accessor.</p>"""
    display_name: NotRequired[
        "aws_sdk_qbusiness.types.data_accessor_name.DataAccessorName"
    ]
    """<p>The updated friendly name for the data accessor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataAccessorRequest) -> dict:
    out: dict = {}
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
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> UpdateDataAccessorRequest:
    out: UpdateDataAccessorRequest = {}  # type: ignore[typeddict-item]
    if "actionConfigurations" in data:
        import aws_sdk_qbusiness.types.action_configuration_list

        out["action_configurations"] = (
            aws_sdk_qbusiness.types.action_configuration_list.deserialize_json(
                data["actionConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataAccessorRequest.action_configurations required"
        )
    if "authenticationDetail" in data:
        import aws_sdk_qbusiness.types.data_accessor_authentication_detail

        out["authentication_detail"] = (
            aws_sdk_qbusiness.types.data_accessor_authentication_detail.deserialize_json(
                data["authenticationDetail"]
            )
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    return out
