"""Generated from Smithy shape ``com.amazonaws.mq#BrokerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.__timestamp_iso8601
    import aws_sdk_mq.types.broker_state
    import aws_sdk_mq.types.deployment_mode
    import aws_sdk_mq.types.engine_type


class BrokerSummary(TypedDict, closed=True):
    broker_arn: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The broker's Amazon Resource Name (ARN).</p>"""
    broker_id: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The unique ID that Amazon MQ generates for the broker.</p>"""
    broker_name: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The broker's name. This value is unique in your Amazon Web Services account, 1-50 characters long, and containing only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters.</p>"""
    broker_state: NotRequired["aws_sdk_mq.types.broker_state.BrokerState"]
    """<p>The broker's status.</p>"""
    created: NotRequired["aws_sdk_mq.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The time when the broker was created.</p>"""
    deployment_mode: NotRequired["aws_sdk_mq.types.deployment_mode.DeploymentMode"]
    """<p>The broker's deployment mode.</p>"""
    engine_type: NotRequired["aws_sdk_mq.types.engine_type.EngineType"]
    """<p>The type of broker engine.</p>"""
    host_instance_type: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The broker's instance type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrokerSummary) -> dict:
    out: dict = {}
    if "broker_arn" in value:
        out["brokerArn"] = value["broker_arn"]
    if "broker_id" in value:
        out["brokerId"] = value["broker_id"]
    if "broker_name" in value:
        out["brokerName"] = value["broker_name"]
    if "broker_state" in value:
        import aws_sdk_mq.types.broker_state

        out["brokerState"] = aws_sdk_mq.types.broker_state.serialize_json(
            value["broker_state"]
        )
    if "created" in value:
        import aws_sdk_mq.types.__timestamp_iso8601

        out["created"] = aws_sdk_mq.types.__timestamp_iso8601.serialize_json(
            value["created"]
        )
    if "deployment_mode" in value:
        import aws_sdk_mq.types.deployment_mode

        out["deploymentMode"] = aws_sdk_mq.types.deployment_mode.serialize_json(
            value["deployment_mode"]
        )
    if "engine_type" in value:
        import aws_sdk_mq.types.engine_type

        out["engineType"] = aws_sdk_mq.types.engine_type.serialize_json(
            value["engine_type"]
        )
    if "host_instance_type" in value:
        out["hostInstanceType"] = value["host_instance_type"]
    return out


def deserialize_json(data: dict) -> BrokerSummary:
    out: BrokerSummary = {}  # type: ignore[typeddict-item]
    if "brokerArn" in data:
        out["broker_arn"] = data["brokerArn"]
    if "brokerId" in data:
        out["broker_id"] = data["brokerId"]
    if "brokerName" in data:
        out["broker_name"] = data["brokerName"]
    if "brokerState" in data:
        import aws_sdk_mq.types.broker_state

        out["broker_state"] = aws_sdk_mq.types.broker_state.deserialize_json(
            data["brokerState"]
        )
    if "created" in data:
        import aws_sdk_mq.types.__timestamp_iso8601

        out["created"] = aws_sdk_mq.types.__timestamp_iso8601.deserialize_json(
            data["created"]
        )
    if "deploymentMode" in data:
        import aws_sdk_mq.types.deployment_mode

        out["deployment_mode"] = aws_sdk_mq.types.deployment_mode.deserialize_json(
            data["deploymentMode"]
        )
    if "engineType" in data:
        import aws_sdk_mq.types.engine_type

        out["engine_type"] = aws_sdk_mq.types.engine_type.deserialize_json(
            data["engineType"]
        )
    if "hostInstanceType" in data:
        out["host_instance_type"] = data["hostInstanceType"]
    return out
