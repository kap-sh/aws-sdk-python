"""Generated from Smithy shape ``com.amazonaws.lakeformation#LFTagError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.error_detail
    import aws_sdk_lakeformation.types.lf_tag_pair


class LFTagError(TypedDict):
    lf_tag: NotRequired["aws_sdk_lakeformation.types.lf_tag_pair.LFTagPair"]
    """<p>The key-name of the LF-tag.</p>"""
    error: NotRequired["aws_sdk_lakeformation.types.error_detail.ErrorDetail"]
    """<p>An error that occurred with the attachment or detachment of the LF-tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LFTagError) -> dict:
    out: dict = {}
    if "lf_tag" in value:
        import aws_sdk_lakeformation.types.lf_tag_pair

        out["LFTag"] = aws_sdk_lakeformation.types.lf_tag_pair.serialize_json(
            value["lf_tag"]
        )
    if "error" in value:
        import aws_sdk_lakeformation.types.error_detail

        out["Error"] = aws_sdk_lakeformation.types.error_detail.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> LFTagError:
    out: LFTagError = {}  # type: ignore[typeddict-item]
    if "LFTag" in data:
        import aws_sdk_lakeformation.types.lf_tag_pair

        out["lf_tag"] = aws_sdk_lakeformation.types.lf_tag_pair.deserialize_json(
            data["LFTag"]
        )
    if "Error" in data:
        import aws_sdk_lakeformation.types.error_detail

        out["error"] = aws_sdk_lakeformation.types.error_detail.deserialize_json(
            data["Error"]
        )
    return out
