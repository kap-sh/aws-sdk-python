"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#VpcLinkVersion``."""

from typing import Literal, TypeAlias, cast

"""<p>The version of the VPC link.</p>"""
VpcLinkVersion: TypeAlias = Literal["V2",]


# --- restJson1 ser/de ---
def serialize_json(value: VpcLinkVersion) -> str:
    return value


def deserialize_json(data: str) -> VpcLinkVersion:
    return cast(VpcLinkVersion, data)
