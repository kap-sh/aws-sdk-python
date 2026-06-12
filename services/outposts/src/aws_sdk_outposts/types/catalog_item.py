"""Generated from Smithy shape ``com.amazonaws.outposts#CatalogItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.catalog_item_power_kva
    import aws_sdk_outposts.types.catalog_item_status
    import aws_sdk_outposts.types.catalog_item_weight_lbs
    import aws_sdk_outposts.types.ec2_capacity_list_definition
    import aws_sdk_outposts.types.sku_code
    import aws_sdk_outposts.types.supported_storage_list
    import aws_sdk_outposts.types.supported_uplink_gbps_list_definition


class CatalogItem(TypedDict):
    catalog_item_id: NotRequired["aws_sdk_outposts.types.sku_code.SkuCode"]
    """<p> The ID of the catalog item. </p>"""
    item_status: NotRequired[
        "aws_sdk_outposts.types.catalog_item_status.CatalogItemStatus"
    ]
    """<p> The status of a catalog item. </p>"""
    ec2_capacities: NotRequired[
        "aws_sdk_outposts.types.ec2_capacity_list_definition.EC2CapacityListDefinition"
    ]
    """<p> Information about the EC2 capacity of an item. </p>"""
    power_kva: NotRequired[
        "aws_sdk_outposts.types.catalog_item_power_kva.CatalogItemPowerKva"
    ]
    """<p> Information about the power draw of an item. </p>"""
    weight_lbs: NotRequired[
        "aws_sdk_outposts.types.catalog_item_weight_lbs.CatalogItemWeightLbs"
    ]
    """<p> The weight of the item in pounds. </p>"""
    supported_uplink_gbps: NotRequired[
        "aws_sdk_outposts.types.supported_uplink_gbps_list_definition.SupportedUplinkGbpsListDefinition"
    ]
    """<p> The uplink speed this catalog item requires for the connection to the Region. </p>"""
    supported_storage: NotRequired[
        "aws_sdk_outposts.types.supported_storage_list.SupportedStorageList"
    ]
    """<p> The supported storage options for the catalog item. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CatalogItem) -> dict:
    out: dict = {}
    if "catalog_item_id" in value:
        out["CatalogItemId"] = value["catalog_item_id"]
    if "item_status" in value:
        import aws_sdk_outposts.types.catalog_item_status

        out["ItemStatus"] = aws_sdk_outposts.types.catalog_item_status.serialize_json(
            value["item_status"]
        )
    if "ec2_capacities" in value:
        import aws_sdk_outposts.types.ec2_capacity_list_definition

        out["EC2Capacities"] = (
            aws_sdk_outposts.types.ec2_capacity_list_definition.serialize_json(
                value["ec2_capacities"]
            )
        )
    if "power_kva" in value:
        out["PowerKva"] = value["power_kva"]
    if "weight_lbs" in value:
        out["WeightLbs"] = value["weight_lbs"]
    if "supported_uplink_gbps" in value:
        import aws_sdk_outposts.types.supported_uplink_gbps_list_definition

        out["SupportedUplinkGbps"] = (
            aws_sdk_outposts.types.supported_uplink_gbps_list_definition.serialize_json(
                value["supported_uplink_gbps"]
            )
        )
    if "supported_storage" in value:
        import aws_sdk_outposts.types.supported_storage_list

        out["SupportedStorage"] = (
            aws_sdk_outposts.types.supported_storage_list.serialize_json(
                value["supported_storage"]
            )
        )
    return out


def deserialize_json(data: dict) -> CatalogItem:
    out: CatalogItem = {}  # type: ignore[typeddict-item]
    if "CatalogItemId" in data:
        out["catalog_item_id"] = data["CatalogItemId"]
    if "ItemStatus" in data:
        import aws_sdk_outposts.types.catalog_item_status

        out["item_status"] = (
            aws_sdk_outposts.types.catalog_item_status.deserialize_json(
                data["ItemStatus"]
            )
        )
    if "EC2Capacities" in data:
        import aws_sdk_outposts.types.ec2_capacity_list_definition

        out["ec2_capacities"] = (
            aws_sdk_outposts.types.ec2_capacity_list_definition.deserialize_json(
                data["EC2Capacities"]
            )
        )
    if "PowerKva" in data:
        out["power_kva"] = data["PowerKva"]
    if "WeightLbs" in data:
        out["weight_lbs"] = data["WeightLbs"]
    if "SupportedUplinkGbps" in data:
        import aws_sdk_outposts.types.supported_uplink_gbps_list_definition

        out["supported_uplink_gbps"] = (
            aws_sdk_outposts.types.supported_uplink_gbps_list_definition.deserialize_json(
                data["SupportedUplinkGbps"]
            )
        )
    if "SupportedStorage" in data:
        import aws_sdk_outposts.types.supported_storage_list

        out["supported_storage"] = (
            aws_sdk_outposts.types.supported_storage_list.deserialize_json(
                data["SupportedStorage"]
            )
        )
    return out
