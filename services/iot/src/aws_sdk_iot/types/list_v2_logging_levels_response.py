"""Generated from Smithy shape ``com.amazonaws.iot#ListV2LoggingLevelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.log_target_configurations
    import aws_sdk_iot.types.next_token


class ListV2LoggingLevelsResponse(TypedDict):
    log_target_configurations: NotRequired[
        "aws_sdk_iot.types.log_target_configurations.LogTargetConfigurations"
    ]
    """<p>The logging configuration for a target.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListV2LoggingLevelsResponse) -> dict:
    out: dict = {}
    if "log_target_configurations" in value:
        import aws_sdk_iot.types.log_target_configurations

        out["logTargetConfigurations"] = (
            aws_sdk_iot.types.log_target_configurations.serialize_json(
                value["log_target_configurations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListV2LoggingLevelsResponse:
    out: ListV2LoggingLevelsResponse = {}  # type: ignore[typeddict-item]
    if "logTargetConfigurations" in data:
        import aws_sdk_iot.types.log_target_configurations

        out["log_target_configurations"] = (
            aws_sdk_iot.types.log_target_configurations.deserialize_json(
                data["logTargetConfigurations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
