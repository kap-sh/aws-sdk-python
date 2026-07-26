"""Generated from Smithy shape ``com.amazonaws.grafana#UpdateErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_grafana.types.update_error

UpdateErrorList: TypeAlias = list["capo_grafana.types.update_error.UpdateError"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateErrorList) -> list:
    import capo_grafana.types.update_error

    out: list = []
    for item in value:
        out.append(capo_grafana.types.update_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateErrorList:
    import capo_grafana.types.update_error

    out: UpdateErrorList = []
    for item in data:
        out.append(capo_grafana.types.update_error.deserialize_json(item))
    return out
