"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ManagedThingAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.account_association_id
    import aws_sdk_iot_managed_integrations.types.managed_thing_association_status
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class ManagedThingAssociation(TypedDict, closed=True):
    managed_thing_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The identifier of the managed thing in the association.</p>"""
    account_association_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    ]
    """<p>The identifier of the account association in the association.</p>"""
    managed_thing_association_status: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_association_status.ManagedThingAssociationStatus"
    ]
    """<p>The status of the registration between the managed thing and the account association. Indicates whether the device is pre-associated or fully associated with the account association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedThingAssociation) -> dict:
    out: dict = {}
    if "managed_thing_id" in value:
        out["ManagedThingId"] = value["managed_thing_id"]
    if "account_association_id" in value:
        out["AccountAssociationId"] = value["account_association_id"]
    if "managed_thing_association_status" in value:
        import aws_sdk_iot_managed_integrations.types.managed_thing_association_status

        out["ManagedThingAssociationStatus"] = (
            aws_sdk_iot_managed_integrations.types.managed_thing_association_status.serialize_json(
                value["managed_thing_association_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedThingAssociation:
    out: ManagedThingAssociation = {}  # type: ignore[typeddict-item]
    if "ManagedThingId" in data:
        out["managed_thing_id"] = data["ManagedThingId"]
    if "AccountAssociationId" in data:
        out["account_association_id"] = data["AccountAssociationId"]
    if "ManagedThingAssociationStatus" in data:
        import aws_sdk_iot_managed_integrations.types.managed_thing_association_status

        out["managed_thing_association_status"] = (
            aws_sdk_iot_managed_integrations.types.managed_thing_association_status.deserialize_json(
                data["ManagedThingAssociationStatus"]
            )
        )
    return out
