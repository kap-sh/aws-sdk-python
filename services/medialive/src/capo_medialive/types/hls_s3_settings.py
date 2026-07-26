"""Generated from Smithy shape ``com.amazonaws.medialive#HlsS3Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.s3_canned_acl


class HlsS3Settings(TypedDict, closed=True):
    canned_acl: NotRequired["capo_medialive.types.s3_canned_acl.S3CannedAcl"]
    """Specify the canned ACL to apply to each S3 request. Defaults to none."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsS3Settings) -> dict:
    out: dict = {}
    if "canned_acl" in value:
        import capo_medialive.types.s3_canned_acl

        out["cannedAcl"] = capo_medialive.types.s3_canned_acl.serialize_json(
            value["canned_acl"]
        )
    return out


def deserialize_json(data: dict) -> HlsS3Settings:
    out: HlsS3Settings = {}  # type: ignore[typeddict-item]
    if "cannedAcl" in data:
        import capo_medialive.types.s3_canned_acl

        out["canned_acl"] = capo_medialive.types.s3_canned_acl.deserialize_json(
            data["cannedAcl"]
        )
    return out
