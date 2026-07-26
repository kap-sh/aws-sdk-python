"""Generated from Smithy shape ``com.amazonaws.m2#ListDeploymentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.deployment_list
    import capo_m2.types.next_token


class ListDeploymentsResponse(TypedDict, closed=True):
    deployments: "capo_m2.types.deployment_list.DeploymentList"
    """<p>The list of deployments that is returned.</p>"""
    next_token: NotRequired["capo_m2.types.next_token.NextToken"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to this operation to retrieve the next set of items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentsResponse) -> dict:
    out: dict = {}
    import capo_m2.types.deployment_list

    out["deployments"] = capo_m2.types.deployment_list.serialize_json(
        value["deployments"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDeploymentsResponse:
    out: ListDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if "deployments" in data:
        import capo_m2.types.deployment_list

        out["deployments"] = capo_m2.types.deployment_list.deserialize_json(
            data["deployments"]
        )
    else:
        raise DeserializationError("ListDeploymentsResponse.deployments required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
