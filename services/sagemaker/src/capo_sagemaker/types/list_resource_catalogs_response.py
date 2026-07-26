"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListResourceCatalogsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.resource_catalog_list


class ListResourceCatalogsResponse(TypedDict, closed=True):
    resource_catalogs: NotRequired[
        "capo_sagemaker.types.resource_catalog_list.ResourceCatalogList"
    ]
    """<p> A list of the requested <code>ResourceCatalog</code>s. </p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p> A token to resume pagination of <code>ListResourceCatalogs</code> results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceCatalogsResponse) -> dict:
    out: dict = {}
    if "resource_catalogs" in value:
        import capo_sagemaker.types.resource_catalog_list

        out["ResourceCatalogs"] = (
            capo_sagemaker.types.resource_catalog_list.serialize_aws_json_1_1(
                value["resource_catalogs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceCatalogsResponse:
    out: ListResourceCatalogsResponse = {}  # type: ignore[typeddict-item]
    if "ResourceCatalogs" in data:
        import capo_sagemaker.types.resource_catalog_list

        out["resource_catalogs"] = (
            capo_sagemaker.types.resource_catalog_list.deserialize_aws_json_1_1(
                data["ResourceCatalogs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
