"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.configuration_state


class DeleteConfigurationResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration.</p>"""
    state: NotRequired["aws_sdk_kafka.types.configuration_state.ConfigurationState"]
    """<p>The state of the configuration. The possible states are ACTIVE, DELETING, and DELETE_FAILED. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "state" in value:
        import aws_sdk_kafka.types.configuration_state

        out["state"] = aws_sdk_kafka.types.configuration_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> DeleteConfigurationResponse:
    out: DeleteConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "state" in data:
        import aws_sdk_kafka.types.configuration_state

        out["state"] = aws_sdk_kafka.types.configuration_state.deserialize_json(
            data["state"]
        )
    return out
