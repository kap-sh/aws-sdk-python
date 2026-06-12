"""Generated from Smithy shape ``com.amazonaws.securityhub#Pages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.page

Pages: TypeAlias = list["aws_sdk_securityhub.types.page.Page"]


# --- restJson1 ser/de ---
def serialize_json(value: Pages) -> list:
    import aws_sdk_securityhub.types.page

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.page.serialize_json(item))
    return out


def deserialize_json(data: list) -> Pages:
    import aws_sdk_securityhub.types.page

    out: Pages = []
    for item in data:
        out.append(aws_sdk_securityhub.types.page.deserialize_json(item))
    return out
