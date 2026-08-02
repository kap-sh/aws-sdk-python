"""Generated from Smithy shape ``com.amazonaws.ec2#GetEbsEncryptionByDefaultResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.sse_type


class GetEbsEncryptionByDefaultResult(TypedDict, closed=True):
    ebs_encryption_by_default: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether encryption by default is enabled.</p>"""
    sse_type: NotRequired["capo_ec2.types.sse_type.SSEType"]
    """<p>Reserved for future use.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetEbsEncryptionByDefaultResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ebs_encryption_by_default" in value:
        pairs.append(
            (
                f"{key_prefix}EbsEncryptionByDefault",
                "true" if value["ebs_encryption_by_default"] else "false",
            )
        )
    if "sse_type" in value:
        import capo_ec2.types.sse_type

        capo_ec2.types.sse_type.serialize_ec2_query(
            value["sse_type"], pairs, f"{key_prefix}SseType"
        )


def deserialize_ec2_query(el: Element) -> GetEbsEncryptionByDefaultResult:
    out: GetEbsEncryptionByDefaultResult = {}  # type: ignore[typeddict-item]
    child_ebs_encryption_by_default = el.find("EbsEncryptionByDefault")
    if child_ebs_encryption_by_default is not None:
        out["ebs_encryption_by_default"] = (
            child_ebs_encryption_by_default.text or ""
        ).lower() == "true"
    child_sse_type = el.find("SseType")
    if child_sse_type is not None:
        import capo_ec2.types.sse_type

        out["sse_type"] = capo_ec2.types.sse_type.deserialize_ec2_query(child_sse_type)
    return out
