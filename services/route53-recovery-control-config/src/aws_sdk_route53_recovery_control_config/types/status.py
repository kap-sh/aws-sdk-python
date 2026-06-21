"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#Status``."""

from typing import Literal, TypeAlias, cast

"""<p>The deployment status of a resource. Status can be one of the following:</p> <p>PENDING: Amazon Route 53 Application Recovery Controller is creating the resource.</p> <p>DEPLOYED: The resource is deployed and ready to use.</p> <p>PENDING_DELETION: Amazon Route 53 Application Recovery Controller is deleting the resource.</p>"""
Status: TypeAlias = Literal[
    "PENDING",
    "DEPLOYED",
    "PENDING_DELETION",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
