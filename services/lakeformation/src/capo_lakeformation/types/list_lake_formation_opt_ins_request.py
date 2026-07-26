"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListLakeFormationOptInsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.page_size
    import capo_lakeformation.types.resource
    import capo_lakeformation.types.token


class ListLakeFormationOptInsRequest(TypedDict, closed=True):
    principal: NotRequired[
        "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
    ]
    resource: NotRequired["capo_lakeformation.types.resource.Resource"]
    """<p>A structure for the resource.</p>"""
    max_results: NotRequired["capo_lakeformation.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is not the first call to retrieve this list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLakeFormationOptInsRequest) -> dict:
    out: dict = {}
    if "principal" in value:
        import capo_lakeformation.types.data_lake_principal

        out["Principal"] = capo_lakeformation.types.data_lake_principal.serialize_json(
            value["principal"]
        )
    if "resource" in value:
        import capo_lakeformation.types.resource

        out["Resource"] = capo_lakeformation.types.resource.serialize_json(
            value["resource"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLakeFormationOptInsRequest:
    out: ListLakeFormationOptInsRequest = {}  # type: ignore[typeddict-item]
    if "Principal" in data:
        import capo_lakeformation.types.data_lake_principal

        out["principal"] = (
            capo_lakeformation.types.data_lake_principal.deserialize_json(
                data["Principal"]
            )
        )
    if "Resource" in data:
        import capo_lakeformation.types.resource

        out["resource"] = capo_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
