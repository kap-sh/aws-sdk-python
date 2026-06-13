"""Generated from Smithy shape ``com.amazonaws.inspector2#Vulnerabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.vulnerability

Vulnerabilities: TypeAlias = list[
    "aws_sdk_inspector2.types.vulnerability.Vulnerability"
]


# --- restJson1 ser/de ---
def serialize_json(value: Vulnerabilities) -> list:
    import aws_sdk_inspector2.types.vulnerability

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.vulnerability.serialize_json(item))
    return out


def deserialize_json(data: list) -> Vulnerabilities:
    import aws_sdk_inspector2.types.vulnerability

    out: Vulnerabilities = []
    for item in data:
        out.append(aws_sdk_inspector2.types.vulnerability.deserialize_json(item))
    return out
