"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#Processor``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_flow_execution_order
    import aws_sdk_chime_sdk_messaging.types.fallback_action
    import aws_sdk_chime_sdk_messaging.types.non_empty_resource_name
    import aws_sdk_chime_sdk_messaging.types.processor_configuration


class Processor(TypedDict, closed=True):
    name: (
        "aws_sdk_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    )
    """<p>The name of the channel flow.</p>"""
    configuration: "aws_sdk_chime_sdk_messaging.types.processor_configuration.ProcessorConfiguration"
    """<p>The information about the type of processor and its identifier.</p>"""
    execution_order: "aws_sdk_chime_sdk_messaging.types.channel_flow_execution_order.ChannelFlowExecutionOrder"
    """<p>The sequence in which processors run. If you have multiple processors in a channel flow, message processing goes through each processor in the sequence. The value determines the sequence. At this point, we support only 1 processor within a flow.</p>"""
    fallback_action: "aws_sdk_chime_sdk_messaging.types.fallback_action.FallbackAction"
    """<p>Determines whether to continue with message processing or stop it in cases where communication with a processor fails. If a processor has a fallback action of <code>ABORT</code> and communication with it fails, the processor sets the message status to <code>FAILED</code> and does not send the message to any recipients. Note that if the last processor in the channel flow sequence has a fallback action of <code>CONTINUE</code> and communication with the processor fails, then the message is considered processed and sent to recipients of the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Processor) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_chime_sdk_messaging.types.processor_configuration

    out["Configuration"] = (
        aws_sdk_chime_sdk_messaging.types.processor_configuration.serialize_json(
            value["configuration"]
        )
    )
    out["ExecutionOrder"] = value["execution_order"]
    import aws_sdk_chime_sdk_messaging.types.fallback_action

    out["FallbackAction"] = (
        aws_sdk_chime_sdk_messaging.types.fallback_action.serialize_json(
            value["fallback_action"]
        )
    )
    return out


def deserialize_json(data: dict) -> Processor:
    out: Processor = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Processor.name required")
    if "Configuration" in data:
        import aws_sdk_chime_sdk_messaging.types.processor_configuration

        out["configuration"] = (
            aws_sdk_chime_sdk_messaging.types.processor_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("Processor.configuration required")
    if "ExecutionOrder" in data:
        out["execution_order"] = data["ExecutionOrder"]
    else:
        raise DeserializationError("Processor.execution_order required")
    if "FallbackAction" in data:
        import aws_sdk_chime_sdk_messaging.types.fallback_action

        out["fallback_action"] = (
            aws_sdk_chime_sdk_messaging.types.fallback_action.deserialize_json(
                data["FallbackAction"]
            )
        )
    else:
        raise DeserializationError("Processor.fallback_action required")
    return out
