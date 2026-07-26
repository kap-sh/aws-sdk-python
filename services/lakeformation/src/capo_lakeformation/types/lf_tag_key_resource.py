"""Generated from Smithy shape ``com.amazonaws.lakeformation#LFTagKeyResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.tag_value_list


class LFTagKeyResource(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    tag_key: "capo_lakeformation.types.name_string.NameString"
    """<p>The key-name for the LF-tag.</p>"""
    tag_values: "capo_lakeformation.types.tag_value_list.TagValueList"
    """<p>A list of possible values an attribute can take.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LFTagKeyResource) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["TagKey"] = value["tag_key"]
    import capo_lakeformation.types.tag_value_list

    out["TagValues"] = capo_lakeformation.types.tag_value_list.serialize_json(
        value["tag_values"]
    )
    return out


def deserialize_json(data: dict) -> LFTagKeyResource:
    out: LFTagKeyResource = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
    else:
        raise DeserializationError("LFTagKeyResource.tag_key required")
    if "TagValues" in data:
        import capo_lakeformation.types.tag_value_list

        out["tag_values"] = capo_lakeformation.types.tag_value_list.deserialize_json(
            data["TagValues"]
        )
    else:
        raise DeserializationError("LFTagKeyResource.tag_values required")
    return out
