"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UpdateAccountAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.account_association_description
    import aws_sdk_iot_managed_integrations.types.account_association_id
    import aws_sdk_iot_managed_integrations.types.account_association_name


class UpdateAccountAssociationRequest(TypedDict, closed=True):
    account_association_id: "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    """<p>The unique identifier of the account association to update.</p>"""
    name: NotRequired[
        "aws_sdk_iot_managed_integrations.types.account_association_name.AccountAssociationName"
    ]
    """<p>The new name to assign to the account association.</p>"""
    description: NotRequired[
        "aws_sdk_iot_managed_integrations.types.account_association_description.AccountAssociationDescription"
    ]
    """<p>The new description to assign to the account association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountAssociationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateAccountAssociationRequest:
    out: UpdateAccountAssociationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
