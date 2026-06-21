"""Generated from Smithy shape ``com.amazonaws.sesv2#Status``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the multi-region endpoint (global-endpoint).</p> <ul> <li> <p> <code>CREATING</code> – The resource is being provisioned.</p> </li> <li> <p> <code>READY</code> – The resource is ready to use.</p> </li> <li> <p> <code>FAILED</code> – The resource failed to be provisioned.</p> </li> <li> <p> <code>DELETING</code> – The resource is being deleted as requested.</p> </li> </ul>"""
Status: TypeAlias = Literal[
    "CREATING",
    "READY",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
