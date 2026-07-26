"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#PostContactSummaryStatus``."""

from typing import Literal, TypeAlias, cast

PostContactSummaryStatus: TypeAlias = Literal[
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PostContactSummaryStatus) -> str:
    return value


def deserialize_json(data: str) -> PostContactSummaryStatus:
    return cast(PostContactSummaryStatus, data)
