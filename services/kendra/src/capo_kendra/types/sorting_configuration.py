"""Generated from Smithy shape ``com.amazonaws.kendra#SortingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.document_attribute_key
    import capo_kendra.types.sort_order


class SortingConfiguration(TypedDict, closed=True):
    document_attribute_key: (
        "capo_kendra.types.document_attribute_key.DocumentAttributeKey"
    )
    """<p>The name of the document attribute used to sort the response. You can use any field that has the <code>Sortable</code> flag set to true.</p> <p>You can also sort by any of the following built-in attributes:</p> <ul> <li> <p>_category</p> </li> <li> <p>_created_at</p> </li> <li> <p>_last_updated_at</p> </li> <li> <p>_version</p> </li> <li> <p>_view_count</p> </li> </ul>"""
    sort_order: "capo_kendra.types.sort_order.SortOrder"
    """<p>The order that the results should be returned in. In case of ties, the relevance assigned to the result by Amazon Kendra is used as the tie-breaker.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortingConfiguration) -> dict:
    out: dict = {}
    out["DocumentAttributeKey"] = value["document_attribute_key"]
    import capo_kendra.types.sort_order

    out["SortOrder"] = capo_kendra.types.sort_order.serialize_aws_json_1_1(
        value["sort_order"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SortingConfiguration:
    out: SortingConfiguration = {}  # type: ignore[typeddict-item]
    if "DocumentAttributeKey" in data:
        out["document_attribute_key"] = data["DocumentAttributeKey"]
    else:
        raise DeserializationError(
            "SortingConfiguration.document_attribute_key required"
        )
    if "SortOrder" in data:
        import capo_kendra.types.sort_order

        out["sort_order"] = capo_kendra.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    else:
        raise DeserializationError("SortingConfiguration.sort_order required")
    return out
