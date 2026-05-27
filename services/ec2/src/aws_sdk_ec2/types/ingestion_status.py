"""Generated from Smithy shape ``com.amazonaws.ec2#IngestionStatus``."""

from typing import Literal, TypeAlias

IngestionStatus: TypeAlias = Literal[
    "initial-ingestion-in-progress",
    "ingestion-complete",
    "ingestion-failed",
]
