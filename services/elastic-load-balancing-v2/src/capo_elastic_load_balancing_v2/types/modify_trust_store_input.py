"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyTrustStoreInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.s3_bucket
    import capo_elastic_load_balancing_v2.types.s3_key
    import capo_elastic_load_balancing_v2.types.s3_object_version
    import capo_elastic_load_balancing_v2.types.trust_store_arn


class ModifyTrustStoreInput(TypedDict, closed=True):
    trust_store_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_arn.TrustStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the trust store.</p>"""
    ca_certificates_bundle_s3_bucket: NotRequired[
        "capo_elastic_load_balancing_v2.types.s3_bucket.S3Bucket"
    ]
    """<p>The Amazon S3 bucket for the ca certificates bundle.</p>"""
    ca_certificates_bundle_s3_key: NotRequired[
        "capo_elastic_load_balancing_v2.types.s3_key.S3Key"
    ]
    """<p>The Amazon S3 path for the ca certificates bundle.</p>"""
    ca_certificates_bundle_s3_object_version: NotRequired[
        "capo_elastic_load_balancing_v2.types.s3_object_version.S3ObjectVersion"
    ]
    """<p>The Amazon S3 object version for the ca certificates bundle. If undefined the current version is used.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyTrustStoreInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "trust_store_arn" in value:
        pairs.append((f"{key_prefix}TrustStoreArn", str(value["trust_store_arn"])))
    if "ca_certificates_bundle_s3_bucket" in value:
        pairs.append(
            (
                f"{key_prefix}CaCertificatesBundleS3Bucket",
                str(value["ca_certificates_bundle_s3_bucket"]),
            )
        )
    if "ca_certificates_bundle_s3_key" in value:
        pairs.append(
            (
                f"{key_prefix}CaCertificatesBundleS3Key",
                str(value["ca_certificates_bundle_s3_key"]),
            )
        )
    if "ca_certificates_bundle_s3_object_version" in value:
        pairs.append(
            (
                f"{key_prefix}CaCertificatesBundleS3ObjectVersion",
                str(value["ca_certificates_bundle_s3_object_version"]),
            )
        )


def deserialize_query(el: Element) -> ModifyTrustStoreInput:
    out: ModifyTrustStoreInput = {}  # type: ignore[typeddict-item]
    child_trust_store_arn = el.find("TrustStoreArn")
    if child_trust_store_arn is not None:
        out["trust_store_arn"] = str(child_trust_store_arn.text or "")
    child_ca_certificates_bundle_s3_bucket = el.find("CaCertificatesBundleS3Bucket")
    if child_ca_certificates_bundle_s3_bucket is not None:
        out["ca_certificates_bundle_s3_bucket"] = str(
            child_ca_certificates_bundle_s3_bucket.text or ""
        )
    child_ca_certificates_bundle_s3_key = el.find("CaCertificatesBundleS3Key")
    if child_ca_certificates_bundle_s3_key is not None:
        out["ca_certificates_bundle_s3_key"] = str(
            child_ca_certificates_bundle_s3_key.text or ""
        )
    child_ca_certificates_bundle_s3_object_version = el.find(
        "CaCertificatesBundleS3ObjectVersion"
    )
    if child_ca_certificates_bundle_s3_object_version is not None:
        out["ca_certificates_bundle_s3_object_version"] = str(
            child_ca_certificates_bundle_s3_object_version.text or ""
        )
    return out
