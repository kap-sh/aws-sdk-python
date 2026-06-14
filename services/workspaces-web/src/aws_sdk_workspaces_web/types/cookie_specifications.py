"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CookieSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.cookie_specification

CookieSpecifications: TypeAlias = list[
    "aws_sdk_workspaces_web.types.cookie_specification.CookieSpecification"
]


# --- restJson1 ser/de ---
def serialize_json(value: CookieSpecifications) -> list:
    import aws_sdk_workspaces_web.types.cookie_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces_web.types.cookie_specification.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CookieSpecifications:
    import aws_sdk_workspaces_web.types.cookie_specification

    out: CookieSpecifications = []
    for item in data:
        out.append(
            aws_sdk_workspaces_web.types.cookie_specification.deserialize_json(item)
        )
    return out
