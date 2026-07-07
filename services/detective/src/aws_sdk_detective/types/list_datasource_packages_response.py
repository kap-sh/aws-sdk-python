"""Generated from Smithy shape ``com.amazonaws.detective#ListDatasourcePackagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.datasource_package_ingest_details
    import aws_sdk_detective.types.pagination_token


class ListDatasourcePackagesResponse(TypedDict, closed=True):
    datasource_packages: NotRequired[
        "aws_sdk_detective.types.datasource_package_ingest_details.DatasourcePackageIngestDetails"
    ]
    """<p>Details on the data source packages active in the behavior graph.</p>"""
    next_token: NotRequired["aws_sdk_detective.types.pagination_token.PaginationToken"]
    """<p>For requests to get the next page of results, the pagination token that was returned with the previous set of results. The initial request does not include a pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasourcePackagesResponse) -> dict:
    out: dict = {}
    if "datasource_packages" in value:
        import aws_sdk_detective.types.datasource_package_ingest_details

        out["DatasourcePackages"] = (
            aws_sdk_detective.types.datasource_package_ingest_details.serialize_json(
                value["datasource_packages"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasourcePackagesResponse:
    out: ListDatasourcePackagesResponse = {}  # type: ignore[typeddict-item]
    if "DatasourcePackages" in data:
        import aws_sdk_detective.types.datasource_package_ingest_details

        out["datasource_packages"] = (
            aws_sdk_detective.types.datasource_package_ingest_details.deserialize_json(
                data["DatasourcePackages"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
