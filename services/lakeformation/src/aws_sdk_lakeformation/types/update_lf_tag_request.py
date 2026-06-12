"""Generated from Smithy shape ``com.amazonaws.lakeformation#UpdateLFTagRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.lf_tag_key
    import aws_sdk_lakeformation.types.tag_value_list


class UpdateLFTagRequest(TypedDict):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    tag_key: "aws_sdk_lakeformation.types.lf_tag_key.LFTagKey"
    """<p>The key-name for the LF-tag for which to add or delete values.</p>"""
    tag_values_to_delete: NotRequired[
        "aws_sdk_lakeformation.types.tag_value_list.TagValueList"
    ]
    """<p>A list of LF-tag values to delete from the LF-tag.</p>"""
    tag_values_to_add: NotRequired[
        "aws_sdk_lakeformation.types.tag_value_list.TagValueList"
    ]
    """<p>A list of LF-tag values to add from the LF-tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLFTagRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["TagKey"] = value["tag_key"]
    if "tag_values_to_delete" in value:
        import aws_sdk_lakeformation.types.tag_value_list

        out["TagValuesToDelete"] = (
            aws_sdk_lakeformation.types.tag_value_list.serialize_json(
                value["tag_values_to_delete"]
            )
        )
    if "tag_values_to_add" in value:
        import aws_sdk_lakeformation.types.tag_value_list

        out["TagValuesToAdd"] = (
            aws_sdk_lakeformation.types.tag_value_list.serialize_json(
                value["tag_values_to_add"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateLFTagRequest:
    out: UpdateLFTagRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
    else:
        raise DeserializationError("UpdateLFTagRequest.tag_key required")
    if "TagValuesToDelete" in data:
        import aws_sdk_lakeformation.types.tag_value_list

        out["tag_values_to_delete"] = (
            aws_sdk_lakeformation.types.tag_value_list.deserialize_json(
                data["TagValuesToDelete"]
            )
        )
    if "TagValuesToAdd" in data:
        import aws_sdk_lakeformation.types.tag_value_list

        out["tag_values_to_add"] = (
            aws_sdk_lakeformation.types.tag_value_list.deserialize_json(
                data["TagValuesToAdd"]
            )
        )
    return out
