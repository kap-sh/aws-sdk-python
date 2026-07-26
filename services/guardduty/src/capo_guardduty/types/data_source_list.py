"""Generated from Smithy shape ``com.amazonaws.guardduty#DataSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.data_source

DataSourceList: TypeAlias = list["capo_guardduty.types.data_source.DataSource"]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceList) -> list:
    import capo_guardduty.types.data_source

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.data_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSourceList:
    import capo_guardduty.types.data_source

    out: DataSourceList = []
    for item in data:
        out.append(capo_guardduty.types.data_source.deserialize_json(item))
    return out
