"""Generated from Smithy shape ``com.amazonaws.connect#ContactMetricResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_metric_result

ContactMetricResults: TypeAlias = list[
    "capo_connect.types.contact_metric_result.ContactMetricResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactMetricResults) -> list:
    import capo_connect.types.contact_metric_result

    out: list = []
    for item in value:
        out.append(capo_connect.types.contact_metric_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactMetricResults:
    import capo_connect.types.contact_metric_result

    out: ContactMetricResults = []
    for item in data:
        out.append(capo_connect.types.contact_metric_result.deserialize_json(item))
    return out
