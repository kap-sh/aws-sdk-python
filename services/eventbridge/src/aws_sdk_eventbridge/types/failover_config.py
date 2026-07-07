"""Generated from Smithy shape ``com.amazonaws.eventbridge#FailoverConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.primary
    import aws_sdk_eventbridge.types.secondary


class FailoverConfig(TypedDict, closed=True):
    primary: "aws_sdk_eventbridge.types.primary.Primary"
    """<p>The main Region of the endpoint.</p>"""
    secondary: "aws_sdk_eventbridge.types.secondary.Secondary"
    """<p>The Region that events are routed to when failover is triggered or event replication is enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailoverConfig) -> dict:
    out: dict = {}
    import aws_sdk_eventbridge.types.primary

    out["Primary"] = aws_sdk_eventbridge.types.primary.serialize_aws_json_1_1(
        value["primary"]
    )
    import aws_sdk_eventbridge.types.secondary

    out["Secondary"] = aws_sdk_eventbridge.types.secondary.serialize_aws_json_1_1(
        value["secondary"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FailoverConfig:
    out: FailoverConfig = {}  # type: ignore[typeddict-item]
    if "Primary" in data:
        import aws_sdk_eventbridge.types.primary

        out["primary"] = aws_sdk_eventbridge.types.primary.deserialize_aws_json_1_1(
            data["Primary"]
        )
    else:
        raise DeserializationError("FailoverConfig.primary required")
    if "Secondary" in data:
        import aws_sdk_eventbridge.types.secondary

        out["secondary"] = aws_sdk_eventbridge.types.secondary.deserialize_aws_json_1_1(
            data["Secondary"]
        )
    else:
        raise DeserializationError("FailoverConfig.secondary required")
    return out
