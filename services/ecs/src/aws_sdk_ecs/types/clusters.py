"""Generated from Smithy shape ``com.amazonaws.ecs#Clusters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.cluster

Clusters: TypeAlias = list["aws_sdk_ecs.types.cluster.Cluster"]
