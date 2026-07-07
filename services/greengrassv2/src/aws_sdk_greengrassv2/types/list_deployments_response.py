"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListDeploymentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.deployment_list
    import aws_sdk_greengrassv2.types.next_token_string


class ListDeploymentsResponse(TypedDict, closed=True):
    deployments: NotRequired[
        "aws_sdk_greengrassv2.types.deployment_list.DeploymentList"
    ]
    """<p>A list that summarizes each deployment.</p>"""
    next_token: NotRequired[
        "aws_sdk_greengrassv2.types.next_token_string.NextTokenString"
    ]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentsResponse) -> dict:
    out: dict = {}
    if "deployments" in value:
        import aws_sdk_greengrassv2.types.deployment_list

        out["deployments"] = aws_sdk_greengrassv2.types.deployment_list.serialize_json(
            value["deployments"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDeploymentsResponse:
    out: ListDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if "deployments" in data:
        import aws_sdk_greengrassv2.types.deployment_list

        out["deployments"] = (
            aws_sdk_greengrassv2.types.deployment_list.deserialize_json(
                data["deployments"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
