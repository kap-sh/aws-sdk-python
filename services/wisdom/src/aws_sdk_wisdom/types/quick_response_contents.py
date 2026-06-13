"""Generated from Smithy shape ``com.amazonaws.wisdom#QuickResponseContents``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.quick_response_content_provider


class QuickResponseContents(TypedDict):
    plain_text: NotRequired[
        "aws_sdk_wisdom.types.quick_response_content_provider.QuickResponseContentProvider"
    ]
    markdown: NotRequired[
        "aws_sdk_wisdom.types.quick_response_content_provider.QuickResponseContentProvider"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseContents) -> dict:
    out: dict = {}
    if "plain_text" in value:
        import aws_sdk_wisdom.types.quick_response_content_provider

        out["plainText"] = (
            aws_sdk_wisdom.types.quick_response_content_provider.serialize_json(
                value["plain_text"]
            )
        )
    if "markdown" in value:
        import aws_sdk_wisdom.types.quick_response_content_provider

        out["markdown"] = (
            aws_sdk_wisdom.types.quick_response_content_provider.serialize_json(
                value["markdown"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuickResponseContents:
    out: QuickResponseContents = {}  # type: ignore[typeddict-item]
    if "plainText" in data:
        import aws_sdk_wisdom.types.quick_response_content_provider

        out["plain_text"] = (
            aws_sdk_wisdom.types.quick_response_content_provider.deserialize_json(
                data["plainText"]
            )
        )
    if "markdown" in data:
        import aws_sdk_wisdom.types.quick_response_content_provider

        out["markdown"] = (
            aws_sdk_wisdom.types.quick_response_content_provider.deserialize_json(
                data["markdown"]
            )
        )
    return out
