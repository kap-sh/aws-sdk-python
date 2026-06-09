"""Generated from Smithy shape ``com.amazonaws.s3#NotificationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.event_bridge_configuration
    import aws_sdk_s3.types.lambda_function_configuration_list
    import aws_sdk_s3.types.queue_configuration_list
    import aws_sdk_s3.types.topic_configuration_list


class NotificationConfiguration(TypedDict):
    topic_configurations: NotRequired[
        "aws_sdk_s3.types.topic_configuration_list.TopicConfigurationList"
    ]
    """<p>The topic to which notifications are sent and the events for which notifications are generated.</p>"""
    queue_configurations: NotRequired[
        "aws_sdk_s3.types.queue_configuration_list.QueueConfigurationList"
    ]
    """<p>The Amazon Simple Queue Service queues to publish messages to and the events for which to publish messages.</p>"""
    lambda_function_configurations: NotRequired[
        "aws_sdk_s3.types.lambda_function_configuration_list.LambdaFunctionConfigurationList"
    ]
    """<p>Describes the Lambda functions to invoke and the events for which to invoke them.</p>"""
    event_bridge_configuration: NotRequired[
        "aws_sdk_s3.types.event_bridge_configuration.EventBridgeConfiguration"
    ]
    """<p>Enables delivery of events to Amazon EventBridge.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: NotificationConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "topic_configurations" in value:
        import aws_sdk_s3.types.topic_configuration_list

        aws_sdk_s3.types.topic_configuration_list.serialize_xml_flat(
            value["topic_configurations"], el, "TopicConfiguration"
        )
    if "queue_configurations" in value:
        import aws_sdk_s3.types.queue_configuration_list

        aws_sdk_s3.types.queue_configuration_list.serialize_xml_flat(
            value["queue_configurations"], el, "QueueConfiguration"
        )
    if "lambda_function_configurations" in value:
        import aws_sdk_s3.types.lambda_function_configuration_list

        aws_sdk_s3.types.lambda_function_configuration_list.serialize_xml_flat(
            value["lambda_function_configurations"], el, "CloudFunctionConfiguration"
        )
    if "event_bridge_configuration" in value:
        import aws_sdk_s3.types.event_bridge_configuration

        aws_sdk_s3.types.event_bridge_configuration.serialize_xml(
            value["event_bridge_configuration"], el, "EventBridgeConfiguration"
        )


def deserialize_xml(el: Element) -> NotificationConfiguration:
    out: NotificationConfiguration = {}  # type: ignore[typeddict-item]
    if el.find("TopicConfiguration") is not None:
        import aws_sdk_s3.types.topic_configuration_list

        out["topic_configurations"] = (
            aws_sdk_s3.types.topic_configuration_list.deserialize_xml_flat(
                el, "TopicConfiguration"
            )
        )
    if el.find("QueueConfiguration") is not None:
        import aws_sdk_s3.types.queue_configuration_list

        out["queue_configurations"] = (
            aws_sdk_s3.types.queue_configuration_list.deserialize_xml_flat(
                el, "QueueConfiguration"
            )
        )
    if el.find("CloudFunctionConfiguration") is not None:
        import aws_sdk_s3.types.lambda_function_configuration_list

        out["lambda_function_configurations"] = (
            aws_sdk_s3.types.lambda_function_configuration_list.deserialize_xml_flat(
                el, "CloudFunctionConfiguration"
            )
        )
    child_event_bridge_configuration = el.find("EventBridgeConfiguration")
    if child_event_bridge_configuration is not None:
        import aws_sdk_s3.types.event_bridge_configuration

        out["event_bridge_configuration"] = (
            aws_sdk_s3.types.event_bridge_configuration.deserialize_xml(
                child_event_bridge_configuration
            )
        )
    return out
