"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketAnalyticsConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.account_id
    import aws_sdk_s3.types.analytics_configuration
    import aws_sdk_s3.types.analytics_id
    import aws_sdk_s3.types.bucket_name


class PutBucketAnalyticsConfigurationRequest(TypedDict):
    bucket: "aws_sdk_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket to which an analytics configuration is stored.</p>"""
    id: "aws_sdk_s3.types.analytics_id.AnalyticsId"
    """<p>The ID that identifies the analytics configuration.</p>"""
    analytics_configuration: (
        "aws_sdk_s3.types.analytics_configuration.AnalyticsConfiguration"
    )
    """<p>The configuration and any analyses for the analytics filter.</p>"""
    expected_bucket_owner: NotRequired["aws_sdk_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutBucketAnalyticsConfigurationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.analytics_configuration

    aws_sdk_s3.types.analytics_configuration.serialize_xml(
        value["analytics_configuration"], el, "AnalyticsConfiguration"
    )


def deserialize_xml(el: Element) -> PutBucketAnalyticsConfigurationRequest:
    out: PutBucketAnalyticsConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_analytics_configuration = el.find("AnalyticsConfiguration")
    if child_analytics_configuration is not None:
        import aws_sdk_s3.types.analytics_configuration

        out["analytics_configuration"] = (
            aws_sdk_s3.types.analytics_configuration.deserialize_xml(
                child_analytics_configuration
            )
        )
    else:
        raise DeserializationError(
            "PutBucketAnalyticsConfigurationRequest.analytics_configuration required"
        )
    return out
