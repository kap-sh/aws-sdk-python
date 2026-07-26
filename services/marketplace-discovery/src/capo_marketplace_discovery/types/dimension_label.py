"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DimensionLabel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.dimension_label_type


class DimensionLabel(TypedDict, closed=True):
    label_type: (
        "capo_marketplace_discovery.types.dimension_label_type.DimensionLabelType"
    )
    """<p>The type of the dimension label, such as <code>Region</code> or <code>SagemakerOption</code>.</p>"""
    label_value: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The value used to group dimensions together.</p>"""
    display_name: NotRequired[
        "capo_marketplace_discovery.types.bounded_string.BoundedString"
    ]
    """<p>The human-readable display name of the label.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DimensionLabel) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.dimension_label_type

    out["labelType"] = (
        capo_marketplace_discovery.types.dimension_label_type.serialize_json(
            value["label_type"]
        )
    )
    out["labelValue"] = value["label_value"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> DimensionLabel:
    out: DimensionLabel = {}  # type: ignore[typeddict-item]
    if "labelType" in data:
        import capo_marketplace_discovery.types.dimension_label_type

        out["label_type"] = (
            capo_marketplace_discovery.types.dimension_label_type.deserialize_json(
                data["labelType"]
            )
        )
    else:
        raise DeserializationError("DimensionLabel.label_type required")
    if "labelValue" in data:
        out["label_value"] = data["labelValue"]
    else:
        raise DeserializationError("DimensionLabel.label_value required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    return out
