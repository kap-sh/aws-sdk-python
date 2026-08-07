"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RevocationContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.revocation_type
    import capo_elastic_load_balancing_v2.types.s3_bucket
    import capo_elastic_load_balancing_v2.types.s3_key
    import capo_elastic_load_balancing_v2.types.s3_object_version


class RevocationContent(TypedDict, closed=True):
    s3_bucket: NotRequired["capo_elastic_load_balancing_v2.types.s3_bucket.S3Bucket"]
    """<p>The Amazon S3 bucket for the revocation file.</p>"""
    s3_key: NotRequired["capo_elastic_load_balancing_v2.types.s3_key.S3Key"]
    """<p>The Amazon S3 path for the revocation file.</p>"""
    s3_object_version: NotRequired[
        "capo_elastic_load_balancing_v2.types.s3_object_version.S3ObjectVersion"
    ]
    """<p>The Amazon S3 object version of the revocation file.</p>"""
    revocation_type: NotRequired[
        "capo_elastic_load_balancing_v2.types.revocation_type.RevocationType"
    ]
    """<p>The type of revocation file.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RevocationContent, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "s3_bucket" in value:
        pairs.append((f"{key_prefix}S3Bucket", str(value["s3_bucket"])))
    if "s3_key" in value:
        pairs.append((f"{key_prefix}S3Key", str(value["s3_key"])))
    if "s3_object_version" in value:
        pairs.append((f"{key_prefix}S3ObjectVersion", str(value["s3_object_version"])))
    if "revocation_type" in value:
        import capo_elastic_load_balancing_v2.types.revocation_type

        capo_elastic_load_balancing_v2.types.revocation_type.serialize_query(
            value["revocation_type"], pairs, f"{key_prefix}RevocationType"
        )


def deserialize_query(el: Element) -> RevocationContent:
    out: RevocationContent = {}  # type: ignore[typeddict-item]
    child_s3_bucket = el.find("S3Bucket")
    if child_s3_bucket is not None:
        out["s3_bucket"] = str(child_s3_bucket.text or "")
    child_s3_key = el.find("S3Key")
    if child_s3_key is not None:
        out["s3_key"] = str(child_s3_key.text or "")
    child_s3_object_version = el.find("S3ObjectVersion")
    if child_s3_object_version is not None:
        out["s3_object_version"] = str(child_s3_object_version.text or "")
    child_revocation_type = el.find("RevocationType")
    if child_revocation_type is not None:
        import capo_elastic_load_balancing_v2.types.revocation_type

        out["revocation_type"] = (
            capo_elastic_load_balancing_v2.types.revocation_type.deserialize_query(
                child_revocation_type
            )
        )
    return out
