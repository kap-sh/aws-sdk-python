"""Generated from Smithy shape ``com.amazonaws.m2#DataSetExportItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.external_location
    import aws_sdk_m2.types.string200


class DataSetExportItem(TypedDict):
    dataset_name: "aws_sdk_m2.types.string200.String200"
    """<p>The data set.</p>"""
    external_location: "aws_sdk_m2.types.external_location.ExternalLocation"
    """<p>The location of the data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetExportItem) -> dict:
    out: dict = {}
    out["datasetName"] = value["dataset_name"]
    import aws_sdk_m2.types.external_location

    out["externalLocation"] = aws_sdk_m2.types.external_location.serialize_json(
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
        import aws_sdk_m2.types.external_location

        out["external_location"] = aws_sdk_m2.types.external_location.deserialize_json(
            data["externalLocation"]
        )
    else:
        raise DeserializationError("DataSetExportItem.external_location required")
    return out
