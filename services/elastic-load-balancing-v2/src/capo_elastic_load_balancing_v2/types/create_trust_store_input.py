"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CreateTrustStoreInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.s3_bucket
    import capo_elastic_load_balancing_v2.types.s3_key
    import capo_elastic_load_balancing_v2.types.s3_object_version
    import capo_elastic_load_balancing_v2.types.tag_list
    import capo_elastic_load_balancing_v2.types.trust_store_name


class CreateTrustStoreInput(TypedDict, closed=True):
    name: NotRequired[
        "capo_elastic_load_balancing_v2.types.trust_store_name.TrustStoreName"
    ]
    """<p>The name of the trust store.</p> <p>This name must be unique per region and can't be changed after creation.</p>"""
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
    tags: NotRequired["capo_elastic_load_balancing_v2.types.tag_list.TagList"]
    """<p>The tags to assign to the trust store.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateTrustStoreInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "ca_certificates_bundle_s3_bucket" in value:
        pairs.append(
            (
                f"{prefix}.CaCertificatesBundleS3Bucket",
                str(value["ca_certificates_bundle_s3_bucket"]),
            )
        )
    if "ca_certificates_bundle_s3_key" in value:
        pairs.append(
            (
                f"{prefix}.CaCertificatesBundleS3Key",
                str(value["ca_certificates_bundle_s3_key"]),
            )
        )
    if "ca_certificates_bundle_s3_object_version" in value:
        pairs.append(
            (
                f"{prefix}.CaCertificatesBundleS3ObjectVersion",
                str(value["ca_certificates_bundle_s3_object_version"]),
            )
        )
    if "tags" in value:
        import capo_elastic_load_balancing_v2.types.tag_list

        capo_elastic_load_balancing_v2.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateTrustStoreInput:
    out: CreateTrustStoreInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
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
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_elastic_load_balancing_v2.types.tag_list

        out["tags"] = capo_elastic_load_balancing_v2.types.tag_list.deserialize_query(
            child_tags
        )
    return out
