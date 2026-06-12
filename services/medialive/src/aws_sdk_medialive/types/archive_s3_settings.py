"""Generated from Smithy shape ``com.amazonaws.medialive#ArchiveS3Settings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.s3_canned_acl


class ArchiveS3Settings(TypedDict):
    canned_acl: NotRequired["aws_sdk_medialive.types.s3_canned_acl.S3CannedAcl"]
    """Specify the canned ACL to apply to each S3 request. Defaults to none."""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveS3Settings) -> dict:
    out: dict = {}
    if "canned_acl" in value:
        import aws_sdk_medialive.types.s3_canned_acl

        out["cannedAcl"] = aws_sdk_medialive.types.s3_canned_acl.serialize_json(
            value["canned_acl"]
        )
    return out


def deserialize_json(data: dict) -> ArchiveS3Settings:
    out: ArchiveS3Settings = {}  # type: ignore[typeddict-item]
    if "cannedAcl" in data:
        import aws_sdk_medialive.types.s3_canned_acl

        out["canned_acl"] = aws_sdk_medialive.types.s3_canned_acl.deserialize_json(
            data["cannedAcl"]
        )
    return out
