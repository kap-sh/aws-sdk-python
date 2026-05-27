"""Generated from Smithy shape ``com.amazonaws.s3#LambdaFunctionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.event_list
    import aws_sdk_s3.types.lambda_function_arn
    import aws_sdk_s3.types.notification_configuration_filter
    import aws_sdk_s3.types.notification_id


class LambdaFunctionConfiguration(TypedDict):
    id: NotRequired["aws_sdk_s3.types.notification_id.NotificationId"]
    lambda_function_arn: "aws_sdk_s3.types.lambda_function_arn.LambdaFunctionArn"
    """<p>The Amazon Resource Name (ARN) of the Lambda function that Amazon S3 invokes when the specified event type occurs.</p>"""
    events: "aws_sdk_s3.types.event_list.EventList"
    """<p>The Amazon S3 bucket event for which to invoke the Lambda function. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html\">Supported Event Types</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    filter: NotRequired[
        "aws_sdk_s3.types.notification_configuration_filter.NotificationConfigurationFilter"
    ]


# --- restXml ser/de ---
def serialize_xml(
    value: LambdaFunctionConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "CloudFunction").text = str(value["lambda_function_arn"])
    import aws_sdk_s3.types.event_list

    aws_sdk_s3.types.event_list.serialize_xml_flat(value["events"], el, "Event")
    if "filter" in value:
        import aws_sdk_s3.types.notification_configuration_filter

        aws_sdk_s3.types.notification_configuration_filter.serialize_xml(
            value["filter"], el, "Filter"
        )


def deserialize_xml(el: Element) -> LambdaFunctionConfiguration:
    out: LambdaFunctionConfiguration = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_lambda_function_arn = el.find("CloudFunction")
    if child_lambda_function_arn is not None:
        out["lambda_function_arn"] = str(child_lambda_function_arn.text or "")
    else:
        raise DeserializationError(
            "LambdaFunctionConfiguration.lambda_function_arn required"
        )
    if el.find("Event") is not None:
        import aws_sdk_s3.types.event_list

        out["events"] = aws_sdk_s3.types.event_list.deserialize_xml_flat(el, "Event")
    else:
        raise DeserializationError("LambdaFunctionConfiguration.events required")
    child_filter = el.find("Filter")
    if child_filter is not None:
        import aws_sdk_s3.types.notification_configuration_filter

        out["filter"] = (
            aws_sdk_s3.types.notification_configuration_filter.deserialize_xml(
                child_filter
            )
        )
    return out
