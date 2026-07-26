"""Generated from Smithy shape ``com.amazonaws.cloudformation#TypeFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.category
    import capo_cloudformation.types.publisher_id
    import capo_cloudformation.types.type_name_prefix


class TypeFilters(TypedDict, closed=True):
    category: NotRequired["capo_cloudformation.types.category.Category"]
    """<p>The category of extensions to return.</p> <ul> <li> <p> <code>REGISTERED</code>: Private extensions that have been registered for this account and Region.</p> </li> <li> <p> <code>ACTIVATED</code>: Public extensions that have been activated for this account and Region.</p> </li> <li> <p> <code>THIRD_PARTY</code>: Extensions available for use from publishers other than Amazon. This includes:</p> <ul> <li> <p>Private extensions registered in the account.</p> </li> <li> <p>Public extensions from publishers other than Amazon, whether activated or not.</p> </li> </ul> </li> <li> <p> <code>AWS_TYPES</code>: Extensions available for use from Amazon.</p> </li> </ul>"""
    publisher_id: NotRequired["capo_cloudformation.types.publisher_id.PublisherId"]
    """<p>The id of the publisher of the extension.</p> <p>Extensions published by Amazon aren't assigned a publisher ID. Use the <code>AWS_TYPES</code> category to specify a list of types published by Amazon.</p>"""
    type_name_prefix: NotRequired[
        "capo_cloudformation.types.type_name_prefix.TypeNamePrefix"
    ]
    """<p>A prefix to use as a filter for results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TypeFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "category" in value:
        import capo_cloudformation.types.category

        capo_cloudformation.types.category.serialize_query(
            value["category"], pairs, f"{prefix}.Category"
        )
    if "publisher_id" in value:
        pairs.append((f"{prefix}.PublisherId", str(value["publisher_id"])))
    if "type_name_prefix" in value:
        pairs.append((f"{prefix}.TypeNamePrefix", str(value["type_name_prefix"])))


def deserialize_query(el: Element) -> TypeFilters:
    out: TypeFilters = {}  # type: ignore[typeddict-item]
    child_category = el.find("Category")
    if child_category is not None:
        import capo_cloudformation.types.category

        out["category"] = capo_cloudformation.types.category.deserialize_query(
            child_category
        )
    child_publisher_id = el.find("PublisherId")
    if child_publisher_id is not None:
        out["publisher_id"] = str(child_publisher_id.text or "")
    child_type_name_prefix = el.find("TypeNamePrefix")
    if child_type_name_prefix is not None:
        out["type_name_prefix"] = str(child_type_name_prefix.text or "")
    return out
