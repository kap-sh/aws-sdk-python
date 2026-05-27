"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaStatus``."""

from typing import Literal, TypeAlias

ReplicaStatus: TypeAlias = Literal[
    "CREATING",
    "CREATION_FAILED",
    "UPDATING",
    "DELETING",
    "ACTIVE",
    "REGION_DISABLED",
    "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
    "ARCHIVING",
    "ARCHIVED",
    "REPLICATION_NOT_AUTHORIZED",
]
