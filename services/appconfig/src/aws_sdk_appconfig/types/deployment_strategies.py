"""Generated from Smithy shape ``com.amazonaws.appconfig#DeploymentStrategies``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.deployment_strategy_list
    import aws_sdk_appconfig.types.next_token


class DeploymentStrategies(TypedDict):
    items: NotRequired[
        "aws_sdk_appconfig.types.deployment_strategy_list.DeploymentStrategyList"
    ]
    """<p>The elements from this collection.</p>"""
    next_token: NotRequired["aws_sdk_appconfig.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStrategies) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_appconfig.types.deployment_strategy_list

        out["Items"] = aws_sdk_appconfig.types.deployment_strategy_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DeploymentStrategies:
    out: DeploymentStrategies = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_appconfig.types.deployment_strategy_list

        out["items"] = (
            aws_sdk_appconfig.types.deployment_strategy_list.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
