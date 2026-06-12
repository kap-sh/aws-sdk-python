"""Generated from Smithy shape ``com.amazonaws.lakeformation#RemoveLFTagsFromResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.lf_tag_errors


class RemoveLFTagsFromResourceResponse(TypedDict):
    failures: NotRequired["aws_sdk_lakeformation.types.lf_tag_errors.LFTagErrors"]
    """<p>A list of failures to untag a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveLFTagsFromResourceResponse) -> dict:
    out: dict = {}
    if "failures" in value:
        import aws_sdk_lakeformation.types.lf_tag_errors

        out["Failures"] = aws_sdk_lakeformation.types.lf_tag_errors.serialize_json(
            value["failures"]
        )
    return out


def deserialize_json(data: dict) -> RemoveLFTagsFromResourceResponse:
    out: RemoveLFTagsFromResourceResponse = {}  # type: ignore[typeddict-item]
    if "Failures" in data:
        import aws_sdk_lakeformation.types.lf_tag_errors

        out["failures"] = aws_sdk_lakeformation.types.lf_tag_errors.deserialize_json(
            data["Failures"]
        )
    return out
