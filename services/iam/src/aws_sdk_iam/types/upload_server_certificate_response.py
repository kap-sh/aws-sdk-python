"""Generated from Smithy shape ``com.amazonaws.iam#UploadServerCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.server_certificate_metadata
    import aws_sdk_iam.types.tag_list_type


class UploadServerCertificateResponse(TypedDict):
    server_certificate_metadata: NotRequired[
        "aws_sdk_iam.types.server_certificate_metadata.ServerCertificateMetadata"
    ]
    """<p>The meta information of the uploaded server certificate without its certificate body, certificate chain, and private key.</p>"""
    tags: NotRequired["aws_sdk_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that are attached to the new IAM server certificate. The returned list of tags is sorted by tag key. For more information about tagging, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html\">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UploadServerCertificateResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "server_certificate_metadata" in value:
        import aws_sdk_iam.types.server_certificate_metadata

        aws_sdk_iam.types.server_certificate_metadata.serialize_query(
            value["server_certificate_metadata"],
            pairs,
            f"{prefix}.ServerCertificateMetadata",
        )
    if "tags" in value:
        import aws_sdk_iam.types.tag_list_type

        aws_sdk_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> UploadServerCertificateResponse:
    out: UploadServerCertificateResponse = {}  # type: ignore[typeddict-item]
    child_server_certificate_metadata = el.find("ServerCertificateMetadata")
    if child_server_certificate_metadata is not None:
        import aws_sdk_iam.types.server_certificate_metadata

        out["server_certificate_metadata"] = (
            aws_sdk_iam.types.server_certificate_metadata.deserialize_query(
                child_server_certificate_metadata
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
