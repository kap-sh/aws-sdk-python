"""Generated from Smithy shape ``com.amazonaws.ecs#PutAccountSettingDefaultResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.setting


class PutAccountSettingDefaultResponse(TypedDict):
    setting: NotRequired["aws_sdk_ecs.types.setting.Setting"]
    """<p>The current setting for a resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAccountSettingDefaultResponse) -> dict:
    out: dict = {}
    if "setting" in value:
        import aws_sdk_ecs.types.setting

        out["setting"] = aws_sdk_ecs.types.setting.serialize_aws_json_1_1(
            value["setting"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAccountSettingDefaultResponse:
    out: PutAccountSettingDefaultResponse = {}  # type: ignore[typeddict-item]
    if "setting" in data:
        import aws_sdk_ecs.types.setting

        out["setting"] = aws_sdk_ecs.types.setting.deserialize_aws_json_1_1(
            data["setting"]
        )
    return out
