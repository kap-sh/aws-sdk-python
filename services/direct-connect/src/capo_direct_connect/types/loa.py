"""Generated from Smithy shape ``com.amazonaws.directconnect#Loa``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.loa_content
    import capo_direct_connect.types.loa_content_type


class Loa(TypedDict, closed=True):
    loa_content: NotRequired["capo_direct_connect.types.loa_content.LoaContent"]
    """<p>The binary contents of the LOA-CFA document.</p>"""
    loa_content_type: NotRequired[
        "capo_direct_connect.types.loa_content_type.LoaContentType"
    ]
    """<p>The standard media type for the LOA-CFA document. The only supported value is application/pdf.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Loa) -> dict:
    out: dict = {}
    if "loa_content" in value:
        import capo_direct_connect.types.loa_content

        out["loaContent"] = (
            capo_direct_connect.types.loa_content.serialize_aws_json_1_1(
                value["loa_content"]
            )
        )
    if "loa_content_type" in value:
        import capo_direct_connect.types.loa_content_type

        out["loaContentType"] = (
            capo_direct_connect.types.loa_content_type.serialize_aws_json_1_1(
                value["loa_content_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Loa:
    out: Loa = {}  # type: ignore[typeddict-item]
    if "loaContent" in data:
        import capo_direct_connect.types.loa_content

        out["loa_content"] = (
            capo_direct_connect.types.loa_content.deserialize_aws_json_1_1(
                data["loaContent"]
            )
        )
    if "loaContentType" in data:
        import capo_direct_connect.types.loa_content_type

        out["loa_content_type"] = (
            capo_direct_connect.types.loa_content_type.deserialize_aws_json_1_1(
                data["loaContentType"]
            )
        )
    return out
