"""Generated from Smithy shape ``com.amazonaws.dsql#ClusterCreationTime``."""

import datetime
from typing import TypeAlias

"""<p>The timestamp when the cluster was created.</p>"""
ClusterCreationTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ClusterCreationTime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> ClusterCreationTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
