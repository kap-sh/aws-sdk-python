"""Generated from Smithy shape ``com.amazonaws.appsync#HandlerConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.handler_behavior
    import aws_sdk_appsync.types.integration


class HandlerConfig(TypedDict):
    behavior: "aws_sdk_appsync.types.handler_behavior.HandlerBehavior"
    """<p>The behavior for the handler.</p>"""
    integration: "aws_sdk_appsync.types.integration.Integration"
    """<p>The integration data source configuration for the handler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HandlerConfig) -> dict:
    out: dict = {}
    import aws_sdk_appsync.types.handler_behavior

    out["behavior"] = aws_sdk_appsync.types.handler_behavior.serialize_json(
        value["behavior"]
    )
    import aws_sdk_appsync.types.integration

    out["integration"] = aws_sdk_appsync.types.integration.serialize_json(
        value["integration"]
    )
    return out


def deserialize_json(data: dict) -> HandlerConfig:
    out: HandlerConfig = {}  # type: ignore[typeddict-item]
    if "behavior" in data:
        import aws_sdk_appsync.types.handler_behavior

        out["behavior"] = aws_sdk_appsync.types.handler_behavior.deserialize_json(
            data["behavior"]
        )
    else:
        raise DeserializationError("HandlerConfig.behavior required")
    if "integration" in data:
        import aws_sdk_appsync.types.integration

        out["integration"] = aws_sdk_appsync.types.integration.deserialize_json(
            data["integration"]
        )
    else:
        raise DeserializationError("HandlerConfig.integration required")
    return out
