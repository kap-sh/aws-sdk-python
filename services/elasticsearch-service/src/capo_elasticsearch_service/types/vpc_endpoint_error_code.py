"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#VpcEndpointErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the error code of the failure encountered while describing the VPC endpoint: <ul> <li>ENDPOINT_NOT_FOUND: Indicates that the requested VPC endpoint does not exist.</li> <li>SERVER_ERROR: Indicates the describe endpoint operation failed due to an internal server error.</li> </ul> </p>"""
VpcEndpointErrorCode: TypeAlias = Literal[
    "ENDPOINT_NOT_FOUND",
    "SERVER_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointErrorCode) -> str:
    return value


def deserialize_json(data: str) -> VpcEndpointErrorCode:
    return cast(VpcEndpointErrorCode, data)
