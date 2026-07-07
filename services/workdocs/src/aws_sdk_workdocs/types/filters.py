"""Generated from Smithy shape ``com.amazonaws.workdocs#Filters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.date_range_type
    import aws_sdk_workdocs.types.long_range_type
    import aws_sdk_workdocs.types.search_ancestor_id_list
    import aws_sdk_workdocs.types.search_collection_type_list
    import aws_sdk_workdocs.types.search_content_category_type_list
    import aws_sdk_workdocs.types.search_label_list
    import aws_sdk_workdocs.types.search_principal_type_list
    import aws_sdk_workdocs.types.search_resource_type_list
    import aws_sdk_workdocs.types.text_locale_type_list


class Filters(TypedDict, closed=True):
    text_locales: NotRequired[
        "aws_sdk_workdocs.types.text_locale_type_list.TextLocaleTypeList"
    ]
    """<p>Filters by the locale of the content or comment.</p>"""
    content_categories: NotRequired[
        "aws_sdk_workdocs.types.search_content_category_type_list.SearchContentCategoryTypeList"
    ]
    """<p>Filters by content category.</p>"""
    resource_types: NotRequired[
        "aws_sdk_workdocs.types.search_resource_type_list.SearchResourceTypeList"
    ]
    """<p>Filters based on entity type.</p>"""
    labels: NotRequired["aws_sdk_workdocs.types.search_label_list.SearchLabelList"]
    """<p>Filter by labels using exact match.</p>"""
    principals: NotRequired[
        "aws_sdk_workdocs.types.search_principal_type_list.SearchPrincipalTypeList"
    ]
    """<p>Filter based on UserIds or GroupIds.</p>"""
    ancestor_ids: NotRequired[
        "aws_sdk_workdocs.types.search_ancestor_id_list.SearchAncestorIdList"
    ]
    """<p>Filter based on resource’s path.</p>"""
    search_collection_types: NotRequired[
        "aws_sdk_workdocs.types.search_collection_type_list.SearchCollectionTypeList"
    ]
    """<p>Filter based on file groupings.</p>"""
    size_range: NotRequired["aws_sdk_workdocs.types.long_range_type.LongRangeType"]
    """<p>Filter based on size (in bytes).</p>"""
    created_range: NotRequired["aws_sdk_workdocs.types.date_range_type.DateRangeType"]
    """<p>Filter based on resource’s creation timestamp.</p>"""
    modified_range: NotRequired["aws_sdk_workdocs.types.date_range_type.DateRangeType"]
    """<p>Filter based on resource’s modified timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filters) -> dict:
    out: dict = {}
    if "text_locales" in value:
        import aws_sdk_workdocs.types.text_locale_type_list

        out["TextLocales"] = (
            aws_sdk_workdocs.types.text_locale_type_list.serialize_json(
                value["text_locales"]
            )
        )
    if "content_categories" in value:
        import aws_sdk_workdocs.types.search_content_category_type_list

        out["ContentCategories"] = (
            aws_sdk_workdocs.types.search_content_category_type_list.serialize_json(
                value["content_categories"]
            )
        )
    if "resource_types" in value:
        import aws_sdk_workdocs.types.search_resource_type_list

        out["ResourceTypes"] = (
            aws_sdk_workdocs.types.search_resource_type_list.serialize_json(
                value["resource_types"]
            )
        )
    if "labels" in value:
        import aws_sdk_workdocs.types.search_label_list

        out["Labels"] = aws_sdk_workdocs.types.search_label_list.serialize_json(
            value["labels"]
        )
    if "principals" in value:
        import aws_sdk_workdocs.types.search_principal_type_list

        out["Principals"] = (
            aws_sdk_workdocs.types.search_principal_type_list.serialize_json(
                value["principals"]
            )
        )
    if "ancestor_ids" in value:
        import aws_sdk_workdocs.types.search_ancestor_id_list

        out["AncestorIds"] = (
            aws_sdk_workdocs.types.search_ancestor_id_list.serialize_json(
                value["ancestor_ids"]
            )
        )
    if "search_collection_types" in value:
        import aws_sdk_workdocs.types.search_collection_type_list

        out["SearchCollectionTypes"] = (
            aws_sdk_workdocs.types.search_collection_type_list.serialize_json(
                value["search_collection_types"]
            )
        )
    if "size_range" in value:
        import aws_sdk_workdocs.types.long_range_type

        out["SizeRange"] = aws_sdk_workdocs.types.long_range_type.serialize_json(
            value["size_range"]
        )
    if "created_range" in value:
        import aws_sdk_workdocs.types.date_range_type

        out["CreatedRange"] = aws_sdk_workdocs.types.date_range_type.serialize_json(
            value["created_range"]
        )
    if "modified_range" in value:
        import aws_sdk_workdocs.types.date_range_type

        out["ModifiedRange"] = aws_sdk_workdocs.types.date_range_type.serialize_json(
            value["modified_range"]
        )
    return out


def deserialize_json(data: dict) -> Filters:
    out: Filters = {}  # type: ignore[typeddict-item]
    if "TextLocales" in data:
        import aws_sdk_workdocs.types.text_locale_type_list

        out["text_locales"] = (
            aws_sdk_workdocs.types.text_locale_type_list.deserialize_json(
                data["TextLocales"]
            )
        )
    if "ContentCategories" in data:
        import aws_sdk_workdocs.types.search_content_category_type_list

        out["content_categories"] = (
            aws_sdk_workdocs.types.search_content_category_type_list.deserialize_json(
                data["ContentCategories"]
            )
        )
    if "ResourceTypes" in data:
        import aws_sdk_workdocs.types.search_resource_type_list

        out["resource_types"] = (
            aws_sdk_workdocs.types.search_resource_type_list.deserialize_json(
                data["ResourceTypes"]
            )
        )
    if "Labels" in data:
        import aws_sdk_workdocs.types.search_label_list

        out["labels"] = aws_sdk_workdocs.types.search_label_list.deserialize_json(
            data["Labels"]
        )
    if "Principals" in data:
        import aws_sdk_workdocs.types.search_principal_type_list

        out["principals"] = (
            aws_sdk_workdocs.types.search_principal_type_list.deserialize_json(
                data["Principals"]
            )
        )
    if "AncestorIds" in data:
        import aws_sdk_workdocs.types.search_ancestor_id_list

        out["ancestor_ids"] = (
            aws_sdk_workdocs.types.search_ancestor_id_list.deserialize_json(
                data["AncestorIds"]
            )
        )
    if "SearchCollectionTypes" in data:
        import aws_sdk_workdocs.types.search_collection_type_list

        out["search_collection_types"] = (
            aws_sdk_workdocs.types.search_collection_type_list.deserialize_json(
                data["SearchCollectionTypes"]
            )
        )
    if "SizeRange" in data:
        import aws_sdk_workdocs.types.long_range_type

        out["size_range"] = aws_sdk_workdocs.types.long_range_type.deserialize_json(
            data["SizeRange"]
        )
    if "CreatedRange" in data:
        import aws_sdk_workdocs.types.date_range_type

        out["created_range"] = aws_sdk_workdocs.types.date_range_type.deserialize_json(
            data["CreatedRange"]
        )
    if "ModifiedRange" in data:
        import aws_sdk_workdocs.types.date_range_type

        out["modified_range"] = aws_sdk_workdocs.types.date_range_type.deserialize_json(
            data["ModifiedRange"]
        )
    return out
