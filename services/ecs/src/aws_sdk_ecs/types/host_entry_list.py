"""Generated from Smithy shape ``com.amazonaws.ecs#HostEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.host_entry

HostEntryList: TypeAlias = list["aws_sdk_ecs.types.host_entry.HostEntry"]
