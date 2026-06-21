"""Generated from Smithy shape ``com.amazonaws.sesv2#HttpsPolicy``."""

from typing import Literal, TypeAlias, cast

"""<p>The https policy to use for tracking open and click events. If the value is OPTIONAL or HttpsPolicy is not specified, the open trackers use HTTP and click tracker use the original protocol of the link. If the value is REQUIRE, both open and click tracker uses HTTPS and if the value is REQUIRE_OPEN_ONLY open tracker uses HTTPS and link tracker is same as original protocol of the link. </p>"""
HttpsPolicy: TypeAlias = Literal[
    "REQUIRE",
    "REQUIRE_OPEN_ONLY",
    "OPTIONAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: HttpsPolicy) -> str:
    return value


def deserialize_json(data: str) -> HttpsPolicy:
    return cast(HttpsPolicy, data)
