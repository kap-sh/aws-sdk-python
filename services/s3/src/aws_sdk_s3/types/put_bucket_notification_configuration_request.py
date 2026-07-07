"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketNotificationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.account_id
    import aws_sdk_s3.types.bucket_name
    import aws_sdk_s3.types.notification_configuration
    import aws_sdk_s3.types.skip_validation


class PutBucketNotificationConfigurationRequest(TypedDict, closed=True):
    bucket: "aws_sdk_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket.</p>"""
    notification_configuration: (
        "aws_sdk_s3.types.notification_configuration.NotificationConfiguration"
    )
    expected_bucket_owner: NotRequired["aws_sdk_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
    skip_destination_validation: NotRequired[
        "aws_sdk_s3.types.skip_validation.SkipValidation"
    ]
    """<p>Skips validation of Amazon SQS, Amazon SNS, and Lambda destinations. True or false value.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutBucketNotificationConfigurationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.notification_configuration

    aws_sdk_s3.types.notification_configuration.serialize_xml(
        value["notification_configuration"], el, "NotificationConfiguration"
    )


def deserialize_xml(el: Element) -> PutBucketNotificationConfigurationRequest:
    out: PutBucketNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_notification_configuration = el.find("NotificationConfiguration")
    if child_notification_configuration is not None:
        import aws_sdk_s3.types.notification_configuration

        out["notification_configuration"] = (
            aws_sdk_s3.types.notification_configuration.deserialize_xml(
                child_notification_configuration
            )
        )
    else:
        raise DeserializationError(
            "PutBucketNotificationConfigurationRequest.notification_configuration required"
        )
    return out
