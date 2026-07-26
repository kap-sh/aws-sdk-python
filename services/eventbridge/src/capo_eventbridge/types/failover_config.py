"""Generated from Smithy shape ``com.amazonaws.eventbridge#FailoverConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.primary
    import capo_eventbridge.types.secondary


class FailoverConfig(TypedDict, closed=True):
    primary: "capo_eventbridge.types.primary.Primary"
    """<p>The main Region of the endpoint.</p>"""
    secondary: "capo_eventbridge.types.secondary.Secondary"
    """<p>The Region that events are routed to when failover is triggered or event replication is enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailoverConfig) -> dict:
    out: dict = {}
    import capo_eventbridge.types.primary

    out["Primary"] = capo_eventbridge.types.primary.serialize_aws_json_1_1(
        value["primary"]
    )
    import capo_eventbridge.types.secondary

    out["Secondary"] = capo_eventbridge.types.secondary.serialize_aws_json_1_1(
        value["secondary"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FailoverConfig:
    out: FailoverConfig = {}  # type: ignore[typeddict-item]
    if "Primary" in data:
        import capo_eventbridge.types.primary

        out["primary"] = capo_eventbridge.types.primary.deserialize_aws_json_1_1(
            data["Primary"]
        )
    else:
        raise DeserializationError("FailoverConfig.primary required")
    if "Secondary" in data:
        import capo_eventbridge.types.secondary

        out["secondary"] = capo_eventbridge.types.secondary.deserialize_aws_json_1_1(
            data["Secondary"]
        )
    else:
        raise DeserializationError("FailoverConfig.secondary required")
    return out
