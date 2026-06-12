"""Generated from Smithy shape ``com.amazonaws.kendra#Search``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.boolean


class Search(TypedDict):
    facetable: "aws_sdk_kendra.types.boolean.Boolean"
    """<p>Indicates that the field can be used to create search facets, a count of results for each value in the field. The default is <code>false</code> .</p>"""
    searchable: "aws_sdk_kendra.types.boolean.Boolean"
    """<p>Determines whether the field is used in the search. If the <code>Searchable</code> field is <code>true</code>, you can use relevance tuning to manually tune how Amazon Kendra weights the field in the search. The default is <code>true</code> for string fields and <code>false</code> for number and date fields.</p>"""
    displayable: "aws_sdk_kendra.types.boolean.Boolean"
    """<p>Determines whether the field is returned in the query response. The default is <code>true</code>.</p>"""
    sortable: "aws_sdk_kendra.types.boolean.Boolean"
    """<p>Determines whether the field can be used to sort the results of a query. If you specify sorting on a field that does not have <code>Sortable</code> set to <code>true</code>, Amazon Kendra returns an exception. The default is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Search) -> dict:
    out: dict = {}
    out["Facetable"] = value.get("facetable", False)
    out["Searchable"] = value.get("searchable", False)
    out["Displayable"] = value.get("displayable", False)
    out["Sortable"] = value.get("sortable", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> Search:
    out: Search = {}  # type: ignore[typeddict-item]
    if "Facetable" in data:
        out["facetable"] = data["Facetable"]
    else:
        out["facetable"] = False
    if "Searchable" in data:
        out["searchable"] = data["Searchable"]
    else:
        out["searchable"] = False
    if "Displayable" in data:
        out["displayable"] = data["Displayable"]
    else:
        out["displayable"] = False
    if "Sortable" in data:
        out["sortable"] = data["Sortable"]
    else:
        out["sortable"] = False
    return out
