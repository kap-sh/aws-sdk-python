"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogS3DestinationOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class VerifiedAccessLogS3DestinationOptions(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether logging is enabled.</p>"""
    bucket_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The bucket name.</p>"""
    prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The bucket prefix.</p>"""
    bucket_owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the Amazon S3 bucket.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessLogS3DestinationOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "enabled" in value:
        pairs.append((f"{prefix}.Enabled", "true" if value["enabled"] else "false"))
    if "bucket_name" in value:
        pairs.append((f"{prefix}.BucketName", str(value["bucket_name"])))
    if "prefix" in value:
        pairs.append((f"{prefix}.Prefix", str(value["prefix"])))
    if "bucket_owner" in value:
        pairs.append((f"{prefix}.BucketOwner", str(value["bucket_owner"])))


def deserialize_ec2_query(el: Element) -> VerifiedAccessLogS3DestinationOptions:
    out: VerifiedAccessLogS3DestinationOptions = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_bucket_name = el.find("BucketName")
    if child_bucket_name is not None:
        out["bucket_name"] = str(child_bucket_name.text or "")
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_bucket_owner = el.find("BucketOwner")
    if child_bucket_owner is not None:
        out["bucket_owner"] = str(child_bucket_owner.text or "")
    return out
