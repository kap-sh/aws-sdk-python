"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteAccountSettingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.setting


class DeleteAccountSettingResponse(TypedDict, closed=True):
    setting: NotRequired["aws_sdk_ecs.types.setting.Setting"]
    """<p>The account setting for the specified principal ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAccountSettingResponse) -> dict:
    out: dict = {}
    if "setting" in value:
        import aws_sdk_ecs.types.setting

        out["setting"] = aws_sdk_ecs.types.setting.serialize_aws_json_1_1(
            value["setting"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAccountSettingResponse:
    out: DeleteAccountSettingResponse = {}  # type: ignore[typeddict-item]
    if "setting" in data:
        import aws_sdk_ecs.types.setting

        out["setting"] = aws_sdk_ecs.types.setting.deserialize_aws_json_1_1(
            data["setting"]
        )
    return out
