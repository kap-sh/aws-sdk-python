"""Generated from Smithy shape ``com.amazonaws.ecs#PutAccountSettingResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.setting


class PutAccountSettingResponse(TypedDict):
    setting: NotRequired["aws_sdk_ecs.types.setting.Setting"]
    """<p>The current account setting for a resource.</p>"""
