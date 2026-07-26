"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MetadataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.metadata_columns_list


class MetadataConfig(TypedDict, closed=True):
    metadata_columns: NotRequired[
        "capo_customer_profiles.types.metadata_columns_list.MetadataColumnsList"
    ]
    """<p>A list of metadata column names from your Items dataset to include in the recommendation response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataConfig) -> dict:
    out: dict = {}
    if "metadata_columns" in value:
        import capo_customer_profiles.types.metadata_columns_list

        out["MetadataColumns"] = (
            capo_customer_profiles.types.metadata_columns_list.serialize_json(
                value["metadata_columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataConfig:
    out: MetadataConfig = {}  # type: ignore[typeddict-item]
    if "MetadataColumns" in data:
        import capo_customer_profiles.types.metadata_columns_list

        out["metadata_columns"] = (
            capo_customer_profiles.types.metadata_columns_list.deserialize_json(
                data["MetadataColumns"]
            )
        )
    return out
