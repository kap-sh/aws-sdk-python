"""Generated from Smithy shape ``com.amazonaws.outposts#CatalogItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.catalog_item_power_kva
    import capo_outposts.types.catalog_item_status
    import capo_outposts.types.catalog_item_weight_lbs
    import capo_outposts.types.ec2_capacity_list_definition
    import capo_outposts.types.sku_code
    import capo_outposts.types.supported_storage_list
    import capo_outposts.types.supported_uplink_gbps_list_definition


class CatalogItem(TypedDict, closed=True):
    catalog_item_id: NotRequired["capo_outposts.types.sku_code.SkuCode"]
    """<p> The ID of the catalog item. </p>"""
    item_status: NotRequired[
        "capo_outposts.types.catalog_item_status.CatalogItemStatus"
    ]
    """<p> The status of a catalog item. </p>"""
    ec2_capacities: NotRequired[
        "capo_outposts.types.ec2_capacity_list_definition.EC2CapacityListDefinition"
    ]
    """<p> Information about the EC2 capacity of an item. </p>"""
    power_kva: NotRequired[
        "capo_outposts.types.catalog_item_power_kva.CatalogItemPowerKva"
    ]
    """<p> Information about the power draw of an item. </p>"""
    weight_lbs: NotRequired[
        "capo_outposts.types.catalog_item_weight_lbs.CatalogItemWeightLbs"
    ]
    """<p> The weight of the item in pounds. </p>"""
    supported_uplink_gbps: NotRequired[
        "capo_outposts.types.supported_uplink_gbps_list_definition.SupportedUplinkGbpsListDefinition"
    ]
    """<p> The uplink speed this catalog item requires for the connection to the Region. </p>"""
    supported_storage: NotRequired[
        "capo_outposts.types.supported_storage_list.SupportedStorageList"
    ]
    """<p> The supported storage options for the catalog item. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CatalogItem) -> dict:
    out: dict = {}
    if "catalog_item_id" in value:
        out["CatalogItemId"] = value["catalog_item_id"]
    if "item_status" in value:
        import capo_outposts.types.catalog_item_status

        out["ItemStatus"] = capo_outposts.types.catalog_item_status.serialize_json(
            value["item_status"]
        )
    if "ec2_capacities" in value:
        import capo_outposts.types.ec2_capacity_list_definition

        out["EC2Capacities"] = (
            capo_outposts.types.ec2_capacity_list_definition.serialize_json(
                value["ec2_capacities"]
            )
        )
    if "power_kva" in value:
        out["PowerKva"] = value["power_kva"]
    if "weight_lbs" in value:
        out["WeightLbs"] = value["weight_lbs"]
    if "supported_uplink_gbps" in value:
        import capo_outposts.types.supported_uplink_gbps_list_definition

        out["SupportedUplinkGbps"] = (
            capo_outposts.types.supported_uplink_gbps_list_definition.serialize_json(
                value["supported_uplink_gbps"]
            )
        )
    if "supported_storage" in value:
        import capo_outposts.types.supported_storage_list

        out["SupportedStorage"] = (
            capo_outposts.types.supported_storage_list.serialize_json(
                value["supported_storage"]
            )
        )
    return out


def deserialize_json(data: dict) -> CatalogItem:
    out: CatalogItem = {}  # type: ignore[typeddict-item]
    if "CatalogItemId" in data:
        out["catalog_item_id"] = data["CatalogItemId"]
    if "ItemStatus" in data:
        import capo_outposts.types.catalog_item_status

        out["item_status"] = capo_outposts.types.catalog_item_status.deserialize_json(
            data["ItemStatus"]
        )
    if "EC2Capacities" in data:
        import capo_outposts.types.ec2_capacity_list_definition

        out["ec2_capacities"] = (
            capo_outposts.types.ec2_capacity_list_definition.deserialize_json(
                data["EC2Capacities"]
            )
        )
    if "PowerKva" in data:
        out["power_kva"] = data["PowerKva"]
    if "WeightLbs" in data:
        out["weight_lbs"] = data["WeightLbs"]
    if "SupportedUplinkGbps" in data:
        import capo_outposts.types.supported_uplink_gbps_list_definition

        out["supported_uplink_gbps"] = (
            capo_outposts.types.supported_uplink_gbps_list_definition.deserialize_json(
                data["SupportedUplinkGbps"]
            )
        )
    if "SupportedStorage" in data:
        import capo_outposts.types.supported_storage_list

        out["supported_storage"] = (
            capo_outposts.types.supported_storage_list.deserialize_json(
                data["SupportedStorage"]
            )
        )
    return out
