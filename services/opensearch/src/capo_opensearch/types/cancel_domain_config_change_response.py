"""Generated from Smithy shape ``com.amazonaws.opensearch#CancelDomainConfigChangeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.cancelled_change_property_list
    import capo_opensearch.types.dry_run
    import capo_opensearch.types.guid_list


class CancelDomainConfigChangeResponse(TypedDict, closed=True):
    cancelled_change_ids: NotRequired["capo_opensearch.types.guid_list.GUIDList"]
    """<p>The unique identifiers of the changes that were cancelled.</p>"""
    cancelled_change_properties: NotRequired[
        "capo_opensearch.types.cancelled_change_property_list.CancelledChangePropertyList"
    ]
    """<p>The domain change properties that were cancelled.</p>"""
    dry_run: NotRequired["capo_opensearch.types.dry_run.DryRun"]
    """<p>Whether or not the request was a dry run. If <code>True</code>, the changes were not actually cancelled. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelDomainConfigChangeResponse) -> dict:
    out: dict = {}
    if "cancelled_change_ids" in value:
        import capo_opensearch.types.guid_list

        out["CancelledChangeIds"] = capo_opensearch.types.guid_list.serialize_json(
            value["cancelled_change_ids"]
        )
    if "cancelled_change_properties" in value:
        import capo_opensearch.types.cancelled_change_property_list

        out["CancelledChangeProperties"] = (
            capo_opensearch.types.cancelled_change_property_list.serialize_json(
                value["cancelled_change_properties"]
            )
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_json(data: dict) -> CancelDomainConfigChangeResponse:
    out: CancelDomainConfigChangeResponse = {}  # type: ignore[typeddict-item]
    if "CancelledChangeIds" in data:
        import capo_opensearch.types.guid_list

        out["cancelled_change_ids"] = capo_opensearch.types.guid_list.deserialize_json(
            data["CancelledChangeIds"]
        )
    if "CancelledChangeProperties" in data:
        import capo_opensearch.types.cancelled_change_property_list

        out["cancelled_change_properties"] = (
            capo_opensearch.types.cancelled_change_property_list.deserialize_json(
                data["CancelledChangeProperties"]
            )
        )
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    return out
