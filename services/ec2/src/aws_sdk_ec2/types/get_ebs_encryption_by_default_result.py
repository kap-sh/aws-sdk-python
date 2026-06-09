"""Generated from Smithy shape ``com.amazonaws.ec2#GetEbsEncryptionByDefaultResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.sse_type


class GetEbsEncryptionByDefaultResult(TypedDict):
    ebs_encryption_by_default: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether encryption by default is enabled.</p>"""
    sse_type: NotRequired["aws_sdk_ec2.types.sse_type.SSEType"]
    """<p>Reserved for future use.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetEbsEncryptionByDefaultResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ebs_encryption_by_default" in value:
        pairs.append(
            (
                f"{prefix}.EbsEncryptionByDefault",
                "true" if value["ebs_encryption_by_default"] else "false",
            )
        )
    if "sse_type" in value:
        import aws_sdk_ec2.types.sse_type

        aws_sdk_ec2.types.sse_type.serialize_ec2_query(
            value["sse_type"], pairs, f"{prefix}.SseType"
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
        import aws_sdk_ec2.types.sse_type

        out["sse_type"] = aws_sdk_ec2.types.sse_type.deserialize_ec2_query(
            child_sse_type
        )
    return out
