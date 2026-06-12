"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CloudWatchLogGroupLogDestination``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.cloud_watch_log_group_arn
    import aws_sdk_lex_models_v2.types.log_prefix


class CloudWatchLogGroupLogDestination(TypedDict):
    cloud_watch_log_group_arn: (
        "aws_sdk_lex_models_v2.types.cloud_watch_log_group_arn.CloudWatchLogGroupArn"
    )
    """<p>The Amazon Resource Name (ARN) of the log group where text and metadata logs are delivered.</p>"""
    log_prefix: "aws_sdk_lex_models_v2.types.log_prefix.LogPrefix"
    """<p>The prefix of the log stream name within the log group that you specified </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogGroupLogDestination) -> dict:
    out: dict = {}
    out["cloudWatchLogGroupArn"] = value["cloud_watch_log_group_arn"]
    out["logPrefix"] = value["log_prefix"]
    return out


def deserialize_json(data: dict) -> CloudWatchLogGroupLogDestination:
    out: CloudWatchLogGroupLogDestination = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogGroupArn" in data:
        out["cloud_watch_log_group_arn"] = data["cloudWatchLogGroupArn"]
    else:
        raise DeserializationError(
            "CloudWatchLogGroupLogDestination.cloud_watch_log_group_arn required"
        )
    if "logPrefix" in data:
        out["log_prefix"] = data["logPrefix"]
    else:
        raise DeserializationError(
            "CloudWatchLogGroupLogDestination.log_prefix required"
        )
    return out
