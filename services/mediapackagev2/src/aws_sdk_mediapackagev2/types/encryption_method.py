"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#EncryptionMethod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.cmaf_encryption_method
    import aws_sdk_mediapackagev2.types.ism_encryption_method
    import aws_sdk_mediapackagev2.types.ts_encryption_method


class EncryptionMethod(TypedDict, closed=True):
    ts_encryption_method: NotRequired[
        "aws_sdk_mediapackagev2.types.ts_encryption_method.TsEncryptionMethod"
    ]
    """<p>The encryption method to use.</p>"""
    cmaf_encryption_method: NotRequired[
        "aws_sdk_mediapackagev2.types.cmaf_encryption_method.CmafEncryptionMethod"
    ]
    """<p>The encryption method to use.</p>"""
    ism_encryption_method: NotRequired[
        "aws_sdk_mediapackagev2.types.ism_encryption_method.IsmEncryptionMethod"
    ]
    """<p>The encryption method used for Microsoft Smooth Streaming (MSS) content. This specifies how the MSS segments are encrypted to protect the content during delivery to client players.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionMethod) -> dict:
    out: dict = {}
    if "ts_encryption_method" in value:
        import aws_sdk_mediapackagev2.types.ts_encryption_method

        out["TsEncryptionMethod"] = (
            aws_sdk_mediapackagev2.types.ts_encryption_method.serialize_json(
                value["ts_encryption_method"]
            )
        )
    if "cmaf_encryption_method" in value:
        import aws_sdk_mediapackagev2.types.cmaf_encryption_method

        out["CmafEncryptionMethod"] = (
            aws_sdk_mediapackagev2.types.cmaf_encryption_method.serialize_json(
                value["cmaf_encryption_method"]
            )
        )
    if "ism_encryption_method" in value:
        import aws_sdk_mediapackagev2.types.ism_encryption_method

        out["IsmEncryptionMethod"] = (
            aws_sdk_mediapackagev2.types.ism_encryption_method.serialize_json(
                value["ism_encryption_method"]
            )
        )
    return out


def deserialize_json(data: dict) -> EncryptionMethod:
    out: EncryptionMethod = {}  # type: ignore[typeddict-item]
    if "TsEncryptionMethod" in data:
        import aws_sdk_mediapackagev2.types.ts_encryption_method

        out["ts_encryption_method"] = (
            aws_sdk_mediapackagev2.types.ts_encryption_method.deserialize_json(
                data["TsEncryptionMethod"]
            )
        )
    if "CmafEncryptionMethod" in data:
        import aws_sdk_mediapackagev2.types.cmaf_encryption_method

        out["cmaf_encryption_method"] = (
            aws_sdk_mediapackagev2.types.cmaf_encryption_method.deserialize_json(
                data["CmafEncryptionMethod"]
            )
        )
    if "IsmEncryptionMethod" in data:
        import aws_sdk_mediapackagev2.types.ism_encryption_method

        out["ism_encryption_method"] = (
            aws_sdk_mediapackagev2.types.ism_encryption_method.deserialize_json(
                data["IsmEncryptionMethod"]
            )
        )
    return out
