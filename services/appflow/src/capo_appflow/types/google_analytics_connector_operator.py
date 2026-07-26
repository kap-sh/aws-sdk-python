"""Generated from Smithy shape ``com.amazonaws.appflow#GoogleAnalyticsConnectorOperator``."""

from typing import Literal, TypeAlias, cast

GoogleAnalyticsConnectorOperator: TypeAlias = Literal[
    "PROJECTION",
    "BETWEEN",
]


# --- restJson1 ser/de ---
def serialize_json(value: GoogleAnalyticsConnectorOperator) -> str:
    return value


def deserialize_json(data: str) -> GoogleAnalyticsConnectorOperator:
    return cast(GoogleAnalyticsConnectorOperator, data)
