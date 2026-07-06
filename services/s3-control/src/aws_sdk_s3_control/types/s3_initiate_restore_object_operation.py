"""Generated from Smithy shape ``com.amazonaws.s3control#S3InitiateRestoreObjectOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_expiration_in_days
    import aws_sdk_s3_control.types.s3_glacier_job_tier


class S3InitiateRestoreObjectOperation(TypedDict, closed=True):
    expiration_in_days: NotRequired[
        "aws_sdk_s3_control.types.s3_expiration_in_days.S3ExpirationInDays"
    ]
    """<p>This argument specifies how long the S3 Glacier or S3 Glacier Deep Archive object remains available in Amazon S3. S3 Initiate Restore Object jobs that target S3 Glacier and S3 Glacier Deep Archive objects require <code>ExpirationInDays</code> set to 1 or greater.</p> <p>Conversely, do <i>not</i> set <code>ExpirationInDays</code> when creating S3 Initiate Restore Object jobs that target S3 Intelligent-Tiering Archive Access and Deep Archive Access tier objects. Objects in S3 Intelligent-Tiering archive access tiers are not subject to restore expiry, so specifying <code>ExpirationInDays</code> results in restore request failure.</p> <p>S3 Batch Operations jobs can operate either on S3 Glacier and S3 Glacier Deep Archive storage class objects or on S3 Intelligent-Tiering Archive Access and Deep Archive Access storage tier objects, but not both types in the same job. If you need to restore objects of both types you <i>must</i> create separate Batch Operations jobs. </p>"""
    glacier_job_tier: NotRequired[
        "aws_sdk_s3_control.types.s3_glacier_job_tier.S3GlacierJobTier"
    ]
    """<p>S3 Batch Operations supports <code>STANDARD</code> and <code>BULK</code> retrieval tiers, but not the <code>EXPEDITED</code> retrieval tier.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: S3InitiateRestoreObjectOperation, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "expiration_in_days" in value:
        SubElement(el, "ExpirationInDays").text = str(value["expiration_in_days"])
    if "glacier_job_tier" in value:
        import aws_sdk_s3_control.types.s3_glacier_job_tier

        aws_sdk_s3_control.types.s3_glacier_job_tier.serialize_xml(
            value["glacier_job_tier"], el, "GlacierJobTier"
        )


def deserialize_xml(el: Element) -> S3InitiateRestoreObjectOperation:
    out: S3InitiateRestoreObjectOperation = {}  # type: ignore[typeddict-item]
    child_expiration_in_days = el.find("ExpirationInDays")
    if child_expiration_in_days is not None:
        out["expiration_in_days"] = int(child_expiration_in_days.text or "")
    child_glacier_job_tier = el.find("GlacierJobTier")
    if child_glacier_job_tier is not None:
        import aws_sdk_s3_control.types.s3_glacier_job_tier

        out["glacier_job_tier"] = (
            aws_sdk_s3_control.types.s3_glacier_job_tier.deserialize_xml(
                child_glacier_job_tier
            )
        )
    return out
