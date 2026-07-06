"""Generated from Smithy shape ``com.amazonaws.eventbridge#RoutingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.failover_config


class RoutingConfig(TypedDict, closed=True):
    failover_config: "aws_sdk_eventbridge.types.failover_config.FailoverConfig"
    """<p>The failover configuration for an endpoint. This includes what triggers failover and what happens when it's triggered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoutingConfig) -> dict:
    out: dict = {}
    import aws_sdk_eventbridge.types.failover_config

    out["FailoverConfig"] = (
        aws_sdk_eventbridge.types.failover_config.serialize_aws_json_1_1(
            value["failover_config"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RoutingConfig:
    out: RoutingConfig = {}  # type: ignore[typeddict-item]
    if "FailoverConfig" in data:
        import aws_sdk_eventbridge.types.failover_config

        out["failover_config"] = (
            aws_sdk_eventbridge.types.failover_config.deserialize_aws_json_1_1(
                data["FailoverConfig"]
            )
        )
    else:
        raise DeserializationError("RoutingConfig.failover_config required")
    return out
