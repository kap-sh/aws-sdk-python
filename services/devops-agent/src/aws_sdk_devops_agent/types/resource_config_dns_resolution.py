"""Generated from Smithy shape ``com.amazonaws.devopsagent#ResourceConfigDnsResolution``."""

from typing import Literal, TypeAlias, cast

"""<p>DNS resolution mode for a Resource Gateway.</p>"""
ResourceConfigDnsResolution: TypeAlias = Literal[
    "PUBLIC",
    "IN_VPC",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConfigDnsResolution) -> str:
    return value


def deserialize_json(data: str) -> ResourceConfigDnsResolution:
    return cast(ResourceConfigDnsResolution, data)
