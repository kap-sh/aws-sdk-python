"""Generated from Smithy shape ``com.amazonaws.m2#DataSetExportItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.external_location
    import capo_m2.types.string200


class DataSetExportItem(TypedDict, closed=True):
    dataset_name: "capo_m2.types.string200.String200"
    """<p>The data set.</p>"""
    external_location: "capo_m2.types.external_location.ExternalLocation"
    """<p>The location of the data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetExportItem) -> dict:
    out: dict = {}
    out["datasetName"] = value["dataset_name"]
    import capo_m2.types.external_location

    out["externalLocation"] = capo_m2.types.external_location.serialize_json(
        value["external_location"]
    )
    return out


def deserialize_json(data: dict) -> DataSetExportItem:
    out: DataSetExportItem = {}  # type: ignore[typeddict-item]
    if "datasetName" in data:
        out["dataset_name"] = data["datasetName"]
    else:
        raise DeserializationError("DataSetExportItem.dataset_name required")
    if "externalLocation" in data:
        import capo_m2.types.external_location

        out["external_location"] = capo_m2.types.external_location.deserialize_json(
            data["externalLocation"]
        )
    else:
        raise DeserializationError("DataSetExportItem.external_location required")
    return out
