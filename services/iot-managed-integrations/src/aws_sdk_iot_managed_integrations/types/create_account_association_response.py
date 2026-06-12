"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateAccountAssociationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.account_association_arn
    import aws_sdk_iot_managed_integrations.types.account_association_id
    import aws_sdk_iot_managed_integrations.types.association_state
    import aws_sdk_iot_managed_integrations.types.o_auth_authorization_url_output


class CreateAccountAssociationResponse(TypedDict):
    o_auth_authorization_url: "aws_sdk_iot_managed_integrations.types.o_auth_authorization_url_output.OAuthAuthorizationUrlOutput"
    """<p>Third-party IoT platform OAuth authorization server URL backed with all the required parameters to perform end-user authentication. This field will be empty when using General Authorization flows that do not require OAuth.</p>"""
    account_association_id: "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    """<p>The identifier for the account association request.</p>"""
    association_state: (
        "aws_sdk_iot_managed_integrations.types.association_state.AssociationState"
    )
    """<p>The current state of the account association request.</p>"""
    arn: NotRequired[
        "aws_sdk_iot_managed_integrations.types.account_association_arn.AccountAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the account association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccountAssociationResponse) -> dict:
    out: dict = {}
    out["OAuthAuthorizationUrl"] = value.get("o_auth_authorization_url", "")
    out["AccountAssociationId"] = value["account_association_id"]
    import aws_sdk_iot_managed_integrations.types.association_state

    out["AssociationState"] = (
        aws_sdk_iot_managed_integrations.types.association_state.serialize_json(
            value["association_state"]
        )
    )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateAccountAssociationResponse:
    out: CreateAccountAssociationResponse = {}  # type: ignore[typeddict-item]
    if "OAuthAuthorizationUrl" in data:
        out["o_auth_authorization_url"] = data["OAuthAuthorizationUrl"]
    else:
        out["o_auth_authorization_url"] = ""
    if "AccountAssociationId" in data:
        out["account_association_id"] = data["AccountAssociationId"]
    else:
        raise DeserializationError(
            "CreateAccountAssociationResponse.account_association_id required"
        )
    if "AssociationState" in data:
        import aws_sdk_iot_managed_integrations.types.association_state

        out["association_state"] = (
            aws_sdk_iot_managed_integrations.types.association_state.deserialize_json(
                data["AssociationState"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAccountAssociationResponse.association_state required"
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
