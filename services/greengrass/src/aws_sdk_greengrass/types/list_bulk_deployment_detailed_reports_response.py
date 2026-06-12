"""Generated from Smithy shape ``com.amazonaws.greengrass#ListBulkDeploymentDetailedReportsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.bulk_deployment_results


class ListBulkDeploymentDetailedReportsResponse(TypedDict):
    deployments: NotRequired[
        "aws_sdk_greengrass.types.bulk_deployment_results.BulkDeploymentResults"
    ]
    """A list of the individual group deployments in the bulk deployment operation."""
    next_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListBulkDeploymentDetailedReportsResponse) -> dict:
    out: dict = {}
    if "deployments" in value:
        import aws_sdk_greengrass.types.bulk_deployment_results

        out["Deployments"] = (
            aws_sdk_greengrass.types.bulk_deployment_results.serialize_json(
                value["deployments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBulkDeploymentDetailedReportsResponse:
    out: ListBulkDeploymentDetailedReportsResponse = {}  # type: ignore[typeddict-item]
    if "Deployments" in data:
        import aws_sdk_greengrass.types.bulk_deployment_results

        out["deployments"] = (
            aws_sdk_greengrass.types.bulk_deployment_results.deserialize_json(
                data["Deployments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
