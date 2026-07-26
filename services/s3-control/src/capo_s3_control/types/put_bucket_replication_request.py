"""Generated from Smithy shape ``com.amazonaws.s3control#PutBucketReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.bucket_name
    import capo_s3_control.types.replication_configuration


class PutBucketReplicationRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the Outposts bucket.</p>"""
    bucket: "capo_s3_control.types.bucket_name.BucketName"
    """<p>Specifies the S3 on Outposts bucket to set the configuration for.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>"""
    replication_configuration: (
        "capo_s3_control.types.replication_configuration.ReplicationConfiguration"
    )
    """<p></p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutBucketReplicationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.replication_configuration

    capo_s3_control.types.replication_configuration.serialize_xml(
        value["replication_configuration"], el, "ReplicationConfiguration"
    )


def deserialize_xml(el: Element) -> PutBucketReplicationRequest:
    out: PutBucketReplicationRequest = {}  # type: ignore[typeddict-item]
    child_replication_configuration = el.find("ReplicationConfiguration")
    if child_replication_configuration is not None:
        import capo_s3_control.types.replication_configuration

        out["replication_configuration"] = (
            capo_s3_control.types.replication_configuration.deserialize_xml(
                child_replication_configuration
            )
        )
    else:
        raise DeserializationError(
            "PutBucketReplicationRequest.replication_configuration required"
        )
    return out
