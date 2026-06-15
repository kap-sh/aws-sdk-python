"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListOnlineEvaluationConfigsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_summary_list


class ListOnlineEvaluationConfigsResponse(TypedDict):
    online_evaluation_configs: "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_summary_list.OnlineEvaluationConfigSummaryList"
    """<p> The list of online evaluation configuration summaries containing basic information about each configuration. </p>"""
    next_token: NotRequired["str"]
    """<p> The pagination token to use in a subsequent request to retrieve the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOnlineEvaluationConfigsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_summary_list

    out["onlineEvaluationConfigs"] = (
        aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_summary_list.serialize_json(
            value["online_evaluation_configs"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOnlineEvaluationConfigsResponse:
    out: ListOnlineEvaluationConfigsResponse = {}  # type: ignore[typeddict-item]
    if "onlineEvaluationConfigs" in data:
        import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_summary_list

        out["online_evaluation_configs"] = (
            aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_summary_list.deserialize_json(
                data["onlineEvaluationConfigs"]
            )
        )
    else:
        raise DeserializationError(
            "ListOnlineEvaluationConfigsResponse.online_evaluation_configs required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
