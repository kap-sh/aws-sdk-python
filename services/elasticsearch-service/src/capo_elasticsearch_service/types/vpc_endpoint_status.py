"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#VpcEndpointStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the current status of the VPC endpoint: <ul> <li>CREATING: Indicates that the VPC endpoint is currently being created.</li> <li>CREATE_FAILED: Indicates that the VPC endpoint creation failed.</li> <li>ACTIVE: Indicates that the VPC endpoint is currently active.</li> <li>UPDATING: Indicates that the VPC endpoint is currently being updated.</li> <li>UPDATE_FAILED: Indicates that the VPC endpoint update failed.</li> <li>DELETING: Indicates that the VPC endpoint is currently being deleted.</li> <li>DELETE_FAILED: Indicates that the VPC endpoint deletion failed.</li> </ul> </p>"""
VpcEndpointStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> VpcEndpointStatus:
    return cast(VpcEndpointStatus, data)
