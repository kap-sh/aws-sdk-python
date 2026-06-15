"""Generated from Smithy shape ``com.amazonaws.ec2#DiskImageDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disk_image_format
    import aws_sdk_ec2.types.import_manifest_url
    import aws_sdk_ec2.types.long


class DiskImageDetail(TypedDict):
    format: NotRequired["aws_sdk_ec2.types.disk_image_format.DiskImageFormat"]
    """<p>The disk image format.</p>"""
    bytes: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The size of the disk image, in GiB.</p>"""
    import_manifest_url: NotRequired[
        "aws_sdk_ec2.types.import_manifest_url.ImportManifestUrl"
    ]
    r"""<p>A presigned URL for the import manifest stored in Amazon S3 and presented here as an Amazon S3 presigned URL. For information about creating a presigned URL for an Amazon S3 object, read the \"Query String Request Authentication Alternative\" section of the <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html\">Authenticating REST Requests</a> topic in the <i>Amazon Simple Storage Service Developer Guide</i>.</p> <p>For information about the import manifest referenced by this API action, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/manifest.html\">VM Import Manifest</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DiskImageDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "format" in value:
        import aws_sdk_ec2.types.disk_image_format

        aws_sdk_ec2.types.disk_image_format.serialize_ec2_query(
            value["format"], pairs, f"{prefix}.Format"
        )
    if "bytes" in value:
        pairs.append((f"{prefix}.Bytes", str(value["bytes"])))
    if "import_manifest_url" in value:
        pairs.append((f"{prefix}.ImportManifestUrl", str(value["import_manifest_url"])))


def deserialize_ec2_query(el: Element) -> DiskImageDetail:
    out: DiskImageDetail = {}  # type: ignore[typeddict-item]
    child_format = el.find("Format")
    if child_format is not None:
        import aws_sdk_ec2.types.disk_image_format

        out["format"] = aws_sdk_ec2.types.disk_image_format.deserialize_ec2_query(
            child_format
        )
    child_bytes = el.find("Bytes")
    if child_bytes is not None:
        out["bytes"] = int(child_bytes.text or "")
    child_import_manifest_url = el.find("ImportManifestUrl")
    if child_import_manifest_url is not None:
        out["import_manifest_url"] = str(child_import_manifest_url.text or "")
    return out
