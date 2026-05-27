"""Generated from Smithy shape ``com.amazonaws.ecs#PutAccountSettingDefaultResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.setting


class PutAccountSettingDefaultResponse(TypedDict):
    setting: NotRequired["aws_sdk_ecs.types.setting.Setting"]
    """<p>The current setting for a resource.</p>"""
