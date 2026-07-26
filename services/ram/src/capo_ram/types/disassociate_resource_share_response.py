"""Generated from Smithy shape ``com.amazonaws.ram#DisassociateResourceShareResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.resource_share_association_list
    import capo_ram.types.string


class DisassociateResourceShareResponse(TypedDict, closed=True):
    resource_share_associations: NotRequired[
        "capo_ram.types.resource_share_association_list.ResourceShareAssociationList"
    ]
    """<p>An array of objects with information about the updated associations for this resource share.</p>"""
    client_token: NotRequired["capo_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateResourceShareResponse) -> dict:
    out: dict = {}
    if "resource_share_associations" in value:
        import capo_ram.types.resource_share_association_list

        out["resourceShareAssociations"] = (
            capo_ram.types.resource_share_association_list.serialize_json(
                value["resource_share_associations"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DisassociateResourceShareResponse:
    out: DisassociateResourceShareResponse = {}  # type: ignore[typeddict-item]
    if "resourceShareAssociations" in data:
        import capo_ram.types.resource_share_association_list

        out["resource_share_associations"] = (
            capo_ram.types.resource_share_association_list.deserialize_json(
                data["resourceShareAssociations"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
