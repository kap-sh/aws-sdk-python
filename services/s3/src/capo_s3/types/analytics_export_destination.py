"""Generated from Smithy shape ``com.amazonaws.s3#AnalyticsExportDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.analytics_s3_bucket_destination


class AnalyticsExportDestination(TypedDict, closed=True):
    s3_bucket_destination: (
        "capo_s3.types.analytics_s3_bucket_destination.AnalyticsS3BucketDestination"
    )
    """<p>A destination signifying output to an S3 bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AnalyticsExportDestination, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.analytics_s3_bucket_destination

    capo_s3.types.analytics_s3_bucket_destination.serialize_xml(
        value["s3_bucket_destination"], el, "S3BucketDestination"
    )


def deserialize_xml(el: Element) -> AnalyticsExportDestination:
    out: AnalyticsExportDestination = {}  # type: ignore[typeddict-item]
    child_s3_bucket_destination = el.find("S3BucketDestination")
    if child_s3_bucket_destination is not None:
        import capo_s3.types.analytics_s3_bucket_destination

        out["s3_bucket_destination"] = (
            capo_s3.types.analytics_s3_bucket_destination.deserialize_xml(
                child_s3_bucket_destination
            )
        )
    else:
        raise DeserializationError(
            "AnalyticsExportDestination.s3_bucket_destination required"
        )
    return out
