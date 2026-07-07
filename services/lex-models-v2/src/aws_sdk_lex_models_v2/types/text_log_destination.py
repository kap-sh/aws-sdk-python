"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TextLogDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.cloud_watch_log_group_log_destination


class TextLogDestination(TypedDict, closed=True):
    cloud_watch: "aws_sdk_lex_models_v2.types.cloud_watch_log_group_log_destination.CloudWatchLogGroupLogDestination"
    """<p>Defines the Amazon CloudWatch Logs log group where text and metadata logs are delivered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextLogDestination) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.cloud_watch_log_group_log_destination

    out["cloudWatch"] = (
        aws_sdk_lex_models_v2.types.cloud_watch_log_group_log_destination.serialize_json(
            value["cloud_watch"]
        )
    )
    return out


def deserialize_json(data: dict) -> TextLogDestination:
    out: TextLogDestination = {}  # type: ignore[typeddict-item]
    if "cloudWatch" in data:
        import aws_sdk_lex_models_v2.types.cloud_watch_log_group_log_destination

        out["cloud_watch"] = (
            aws_sdk_lex_models_v2.types.cloud_watch_log_group_log_destination.deserialize_json(
                data["cloudWatch"]
            )
        )
    else:
        raise DeserializationError("TextLogDestination.cloud_watch required")
    return out
