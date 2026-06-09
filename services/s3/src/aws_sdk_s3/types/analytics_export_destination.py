"""Generated from Smithy shape ``com.amazonaws.s3#AnalyticsExportDestination``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.analytics_s3_bucket_destination


class AnalyticsExportDestination(TypedDict):
    s3_bucket_destination: (
        "aws_sdk_s3.types.analytics_s3_bucket_destination.AnalyticsS3BucketDestination"
    )
    """<p>A destination signifying output to an S3 bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AnalyticsExportDestination, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.analytics_s3_bucket_destination

    aws_sdk_s3.types.analytics_s3_bucket_destination.serialize_xml(
        value["s3_bucket_destination"], el, "S3BucketDestination"
    )


def deserialize_xml(el: Element) -> AnalyticsExportDestination:
    out: AnalyticsExportDestination = {}  # type: ignore[typeddict-item]
    child_s3_bucket_destination = el.find("S3BucketDestination")
    if child_s3_bucket_destination is not None:
        import aws_sdk_s3.types.analytics_s3_bucket_destination

        out["s3_bucket_destination"] = (
            aws_sdk_s3.types.analytics_s3_bucket_destination.deserialize_xml(
                child_s3_bucket_destination
            )
        )
    else:
        raise DeserializationError(
            "AnalyticsExportDestination.s3_bucket_destination required"
        )
    return out
