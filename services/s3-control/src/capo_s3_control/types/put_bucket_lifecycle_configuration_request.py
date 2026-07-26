"""Generated from Smithy shape ``com.amazonaws.s3control#PutBucketLifecycleConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.bucket_name
    import capo_s3_control.types.lifecycle_configuration


class PutBucketLifecycleConfigurationRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the Outposts bucket.</p>"""
    bucket: "capo_s3_control.types.bucket_name.BucketName"
    """<p>The name of the bucket for which to set the configuration.</p>"""
    lifecycle_configuration: NotRequired[
        "capo_s3_control.types.lifecycle_configuration.LifecycleConfiguration"
    ]
    """<p>Container for lifecycle rules. You can add as many as 1,000 rules.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutBucketLifecycleConfigurationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "lifecycle_configuration" in value:
        import capo_s3_control.types.lifecycle_configuration

        capo_s3_control.types.lifecycle_configuration.serialize_xml(
            value["lifecycle_configuration"], el, "LifecycleConfiguration"
        )


def deserialize_xml(el: Element) -> PutBucketLifecycleConfigurationRequest:
    out: PutBucketLifecycleConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_lifecycle_configuration = el.find("LifecycleConfiguration")
    if child_lifecycle_configuration is not None:
        import capo_s3_control.types.lifecycle_configuration

        out["lifecycle_configuration"] = (
            capo_s3_control.types.lifecycle_configuration.deserialize_xml(
                child_lifecycle_configuration
            )
        )
    return out
