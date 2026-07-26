"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilderStateChangeReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.app_block_builder_state_change_reason_code
    import capo_appstream.types.string


class AppBlockBuilderStateChangeReason(TypedDict, closed=True):
    code: NotRequired[
        "capo_appstream.types.app_block_builder_state_change_reason_code.AppBlockBuilderStateChangeReasonCode"
    ]
    """<p>The state change reason code.</p>"""
    message: NotRequired["capo_appstream.types.string.String"]
    """<p>The state change reason message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppBlockBuilderStateChangeReason) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_appstream.types.app_block_builder_state_change_reason_code

        out["Code"] = (
            capo_appstream.types.app_block_builder_state_change_reason_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AppBlockBuilderStateChangeReason:
    out: AppBlockBuilderStateChangeReason = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import capo_appstream.types.app_block_builder_state_change_reason_code

        out["code"] = (
            capo_appstream.types.app_block_builder_state_change_reason_code.deserialize_aws_json_1_1(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
