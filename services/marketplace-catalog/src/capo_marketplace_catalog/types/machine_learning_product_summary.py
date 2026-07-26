"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#MachineLearningProductSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.machine_learning_product_title_string
    import capo_marketplace_catalog.types.machine_learning_product_visibility_string


class MachineLearningProductSummary(TypedDict, closed=True):
    product_title: NotRequired[
        "capo_marketplace_catalog.types.machine_learning_product_title_string.MachineLearningProductTitleString"
    ]
    """<p>The title of the machine learning product.</p>"""
    visibility: NotRequired[
        "capo_marketplace_catalog.types.machine_learning_product_visibility_string.MachineLearningProductVisibilityString"
    ]
    """<p>The visibility status of the machine learning product. Valid values are <code>Limited</code>, <code>Public</code>, <code>Restricted</code>, and <code>Draft</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MachineLearningProductSummary) -> dict:
    out: dict = {}
    if "product_title" in value:
        out["ProductTitle"] = value["product_title"]
    if "visibility" in value:
        import capo_marketplace_catalog.types.machine_learning_product_visibility_string

        out["Visibility"] = (
            capo_marketplace_catalog.types.machine_learning_product_visibility_string.serialize_json(
                value["visibility"]
            )
        )
    return out


def deserialize_json(data: dict) -> MachineLearningProductSummary:
    out: MachineLearningProductSummary = {}  # type: ignore[typeddict-item]
    if "ProductTitle" in data:
        out["product_title"] = data["ProductTitle"]
    if "Visibility" in data:
        import capo_marketplace_catalog.types.machine_learning_product_visibility_string

        out["visibility"] = (
            capo_marketplace_catalog.types.machine_learning_product_visibility_string.deserialize_json(
                data["Visibility"]
            )
        )
    return out
