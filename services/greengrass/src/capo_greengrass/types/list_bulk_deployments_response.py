"""Generated from Smithy shape ``com.amazonaws.greengrass#ListBulkDeploymentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.bulk_deployments


class ListBulkDeploymentsResponse(TypedDict, closed=True):
    bulk_deployments: NotRequired[
        "capo_greengrass.types.bulk_deployments.BulkDeployments"
    ]
    """A list of bulk deployments."""
    next_token: NotRequired["capo_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListBulkDeploymentsResponse) -> dict:
    out: dict = {}
    if "bulk_deployments" in value:
        import capo_greengrass.types.bulk_deployments

        out["BulkDeployments"] = capo_greengrass.types.bulk_deployments.serialize_json(
            value["bulk_deployments"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBulkDeploymentsResponse:
    out: ListBulkDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if "BulkDeployments" in data:
        import capo_greengrass.types.bulk_deployments

        out["bulk_deployments"] = (
            capo_greengrass.types.bulk_deployments.deserialize_json(
                data["BulkDeployments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
