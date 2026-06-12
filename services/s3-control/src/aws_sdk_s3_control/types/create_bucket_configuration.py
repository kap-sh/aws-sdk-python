"""Generated from Smithy shape ``com.amazonaws.s3control#CreateBucketConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.bucket_location_constraint


class CreateBucketConfiguration(TypedDict):
    location_constraint: NotRequired[
        "aws_sdk_s3_control.types.bucket_location_constraint.BucketLocationConstraint"
    ]
    """<p>Specifies the Region where the bucket will be created. If you are creating a bucket on the US East (N. Virginia) Region (us-east-1), you do not need to specify the location. </p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateBucketConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "location_constraint" in value:
        import aws_sdk_s3_control.types.bucket_location_constraint

        aws_sdk_s3_control.types.bucket_location_constraint.serialize_xml(
            value["location_constraint"], el, "LocationConstraint"
        )


def deserialize_xml(el: Element) -> CreateBucketConfiguration:
    out: CreateBucketConfiguration = {}  # type: ignore[typeddict-item]
    child_location_constraint = el.find("LocationConstraint")
    if child_location_constraint is not None:
        import aws_sdk_s3_control.types.bucket_location_constraint

        out["location_constraint"] = (
            aws_sdk_s3_control.types.bucket_location_constraint.deserialize_xml(
                child_location_constraint
            )
        )
    return out
