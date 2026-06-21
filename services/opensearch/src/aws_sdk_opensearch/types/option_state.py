"""Generated from Smithy shape ``com.amazonaws.opensearch#OptionState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a requested domain configuration change. Can be one of the following:</p> <ul> <li> <p> <b>Processing</b> - The requested change is still in progress.</p> </li> <li> <p> <b>Active</b> - The requested change is processed and deployed to the domain.</p> </li> </ul>"""
OptionState: TypeAlias = Literal[
    "RequiresIndexDocuments",
    "Processing",
    "Active",
]


# --- restJson1 ser/de ---
def serialize_json(value: OptionState) -> str:
    return value


def deserialize_json(data: str) -> OptionState:
    return cast(OptionState, data)
