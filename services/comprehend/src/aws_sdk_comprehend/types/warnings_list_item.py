"""Generated from Smithy shape ``com.amazonaws.comprehend#WarningsListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.page_based_warning_code
    import aws_sdk_comprehend.types.string


class WarningsListItem(TypedDict):
    page: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>Page number in the input document.</p>"""
    warn_code: NotRequired[
        "aws_sdk_comprehend.types.page_based_warning_code.PageBasedWarningCode"
    ]
    """<p>The type of warning.</p>"""
    warn_message: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Text message associated with the warning.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WarningsListItem) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "warn_code" in value:
        import aws_sdk_comprehend.types.page_based_warning_code

        out["WarnCode"] = (
            aws_sdk_comprehend.types.page_based_warning_code.serialize_aws_json_1_1(
                value["warn_code"]
            )
        )
    if "warn_message" in value:
        out["WarnMessage"] = value["warn_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WarningsListItem:
    out: WarningsListItem = {}  # type: ignore[typeddict-item]
    if "Page" in data:
        out["page"] = data["Page"]
    if "WarnCode" in data:
        import aws_sdk_comprehend.types.page_based_warning_code

        out["warn_code"] = (
            aws_sdk_comprehend.types.page_based_warning_code.deserialize_aws_json_1_1(
                data["WarnCode"]
            )
        )
    if "WarnMessage" in data:
        out["warn_message"] = data["WarnMessage"]
    return out
