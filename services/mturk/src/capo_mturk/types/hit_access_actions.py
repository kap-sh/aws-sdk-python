"""Generated from Smithy shape ``com.amazonaws.mturk#HITAccessActions``."""

from typing import Literal, TypeAlias, cast

HITAccessActions: TypeAlias = Literal[
    "Accept",
    "PreviewAndAccept",
    "DiscoverPreviewAndAccept",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HITAccessActions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HITAccessActions:
    return cast(HITAccessActions, data)
