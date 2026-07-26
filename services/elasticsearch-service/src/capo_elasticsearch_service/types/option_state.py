"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#OptionState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a requested change. One of the following:</p> <ul> <li>Processing: The request change is still in-process.</li> <li>Active: The request change is processed and deployed to the Elasticsearch domain.</li> </ul>"""
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
