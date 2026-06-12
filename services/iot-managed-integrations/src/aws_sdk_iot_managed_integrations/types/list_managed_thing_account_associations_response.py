"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListManagedThingAccountAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.managed_thing_association_list


class ListManagedThingAccountAssociationsResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_association_list.ManagedThingAssociationList"
    ]
    """<p>The list of managed thing associations that match the specified criteria, including the managed thing ID and account association ID for each association.</p>"""
    next_token: NotRequired["str"]
    """<p>A token used for pagination of results when there are more account associations than can be returned in a single response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedThingAccountAssociationsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_iot_managed_integrations.types.managed_thing_association_list

        out["Items"] = (
            aws_sdk_iot_managed_integrations.types.managed_thing_association_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListManagedThingAccountAssociationsResponse:
    out: ListManagedThingAccountAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_iot_managed_integrations.types.managed_thing_association_list

        out["items"] = (
            aws_sdk_iot_managed_integrations.types.managed_thing_association_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
