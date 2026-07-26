"""Generated from Smithy shape ``com.amazonaws.cloudtrail#PublicKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.byte_buffer
    import capo_cloudtrail.types.date
    import capo_cloudtrail.types.string


class PublicKey(TypedDict, closed=True):
    value: NotRequired["capo_cloudtrail.types.byte_buffer.ByteBuffer"]
    """<p>The DER encoded public key value in PKCS#1 format.</p>"""
    validity_start_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>The starting time of validity of the public key.</p>"""
    validity_end_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>The ending time of validity of the public key.</p>"""
    fingerprint: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>The fingerprint of the public key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicKey) -> dict:
    out: dict = {}
    if "value" in value:
        import capo_cloudtrail.types.byte_buffer

        out["Value"] = capo_cloudtrail.types.byte_buffer.serialize_aws_json_1_1(
            value["value"]
        )
    if "validity_start_time" in value:
        import capo_cloudtrail.types.date

        out["ValidityStartTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["validity_start_time"]
        )
    if "validity_end_time" in value:
        import capo_cloudtrail.types.date

        out["ValidityEndTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["validity_end_time"]
        )
    if "fingerprint" in value:
        out["Fingerprint"] = value["fingerprint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PublicKey:
    out: PublicKey = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        import capo_cloudtrail.types.byte_buffer

        out["value"] = capo_cloudtrail.types.byte_buffer.deserialize_aws_json_1_1(
            data["Value"]
        )
    if "ValidityStartTime" in data:
        import capo_cloudtrail.types.date

        out["validity_start_time"] = (
            capo_cloudtrail.types.date.deserialize_aws_json_1_1(
                data["ValidityStartTime"]
            )
        )
    if "ValidityEndTime" in data:
        import capo_cloudtrail.types.date

        out["validity_end_time"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["ValidityEndTime"]
        )
    if "Fingerprint" in data:
        out["fingerprint"] = data["Fingerprint"]
    return out
