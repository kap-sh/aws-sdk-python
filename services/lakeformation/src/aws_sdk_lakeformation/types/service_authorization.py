"""Generated from Smithy shape ``com.amazonaws.lakeformation#ServiceAuthorization``."""

from typing import Literal, TypeAlias, cast

"""<p>Authorization status for service integrations. Specify a value of <code>ENABLED</code> or <code>DISABLED</code>.</p>"""
ServiceAuthorization: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceAuthorization) -> str:
    return value


def deserialize_json(data: str) -> ServiceAuthorization:
    return cast(ServiceAuthorization, data)
