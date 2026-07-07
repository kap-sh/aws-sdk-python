"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_summaries
    import aws_sdk_service_catalog_appregistry.types.next_token


class ListApplicationsResponse(TypedDict, closed=True):
    applications: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.application_summaries.ApplicationSummaries"
    ]
    """<p>This list of applications.</p>"""
    next_token: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.next_token.NextToken"
    ]
    """<p>The token to use to get the next page of results after a previous API call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    if "applications" in value:
        import aws_sdk_service_catalog_appregistry.types.application_summaries

        out["applications"] = (
            aws_sdk_service_catalog_appregistry.types.application_summaries.serialize_json(
                value["applications"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "applications" in data:
        import aws_sdk_service_catalog_appregistry.types.application_summaries

        out["applications"] = (
            aws_sdk_service_catalog_appregistry.types.application_summaries.deserialize_json(
                data["applications"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
