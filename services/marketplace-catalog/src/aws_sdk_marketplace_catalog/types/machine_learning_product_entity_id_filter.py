"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#MachineLearningProductEntityIdFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.machine_learning_product_entity_id_filter_value_list


class MachineLearningProductEntityIdFilter(TypedDict):
    value_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.machine_learning_product_entity_id_filter_value_list.MachineLearningProductEntityIdFilterValueList"
    ]
    """<p>A list of entity IDs to filter by. The operation returns machine learning products with entity IDs that match the values in this list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MachineLearningProductEntityIdFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_entity_id_filter_value_list

        out["ValueList"] = (
            aws_sdk_marketplace_catalog.types.machine_learning_product_entity_id_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> MachineLearningProductEntityIdFilter:
    out: MachineLearningProductEntityIdFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_entity_id_filter_value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.machine_learning_product_entity_id_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
