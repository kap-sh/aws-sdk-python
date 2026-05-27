"""Generated from Smithy shape ``com.amazonaws.ec2#LogDestinationType``."""

from typing import Literal, TypeAlias

LogDestinationType: TypeAlias = Literal[
    "cloud-watch-logs",
    "s3",
    "kinesis-data-firehose",
]
