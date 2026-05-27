"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableStatus``."""

from typing import Literal, TypeAlias

TableStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "ACTIVE",
    "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
    "ARCHIVING",
    "ARCHIVED",
    "REPLICATION_NOT_AUTHORIZED",
]
