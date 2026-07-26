"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#IntegrationType``."""

from typing import Literal, TypeAlias, cast

"""<p>Represents an API method integration type.</p>"""
IntegrationType: TypeAlias = Literal[
    "AWS",
    "HTTP",
    "MOCK",
    "HTTP_PROXY",
    "AWS_PROXY",
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationType) -> str:
    return value


def deserialize_json(data: str) -> IntegrationType:
    return cast(IntegrationType, data)
