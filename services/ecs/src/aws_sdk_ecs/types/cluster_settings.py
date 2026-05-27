"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.cluster_setting

ClusterSettings: TypeAlias = list["aws_sdk_ecs.types.cluster_setting.ClusterSetting"]
