"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketIntelligentTieringConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.intelligent_tiering_configuration
    import capo_s3.types.intelligent_tiering_id


class PutBucketIntelligentTieringConfigurationRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the Amazon S3 bucket whose configuration you want to modify or retrieve.</p>"""
    id: "capo_s3.types.intelligent_tiering_id.IntelligentTieringId"
    """<p>The ID used to identify the S3 Intelligent-Tiering configuration.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
    intelligent_tiering_configuration: "capo_s3.types.intelligent_tiering_configuration.IntelligentTieringConfiguration"
    """<p>Container for S3 Intelligent-Tiering configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutBucketIntelligentTieringConfigurationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.intelligent_tiering_configuration

    capo_s3.types.intelligent_tiering_configuration.serialize_xml(
        value["intelligent_tiering_configuration"],
        el,
        "IntelligentTieringConfiguration",
    )


def deserialize_xml(el: Element) -> PutBucketIntelligentTieringConfigurationRequest:
    out: PutBucketIntelligentTieringConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_intelligent_tiering_configuration = el.find("IntelligentTieringConfiguration")
    if child_intelligent_tiering_configuration is not None:
        import capo_s3.types.intelligent_tiering_configuration

        out["intelligent_tiering_configuration"] = (
            capo_s3.types.intelligent_tiering_configuration.deserialize_xml(
                child_intelligent_tiering_configuration
            )
        )
    else:
        raise DeserializationError(
            "PutBucketIntelligentTieringConfigurationRequest.intelligent_tiering_configuration required"
        )
    return out
