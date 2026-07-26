"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.import_data_source
    import capo_sesv2.types.import_destination


class CreateImportJobRequest(TypedDict, closed=True):
    import_destination: "capo_sesv2.types.import_destination.ImportDestination"
    """<p>The destination for the import job.</p>"""
    import_data_source: "capo_sesv2.types.import_data_source.ImportDataSource"
    """<p>The data source for the import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateImportJobRequest) -> dict:
    out: dict = {}
    import capo_sesv2.types.import_destination

    out["ImportDestination"] = capo_sesv2.types.import_destination.serialize_json(
        value["import_destination"]
    )
    import capo_sesv2.types.import_data_source

    out["ImportDataSource"] = capo_sesv2.types.import_data_source.serialize_json(
        value["import_data_source"]
    )
    return out


def deserialize_json(data: dict) -> CreateImportJobRequest:
    out: CreateImportJobRequest = {}  # type: ignore[typeddict-item]
    if "ImportDestination" in data:
        import capo_sesv2.types.import_destination

        out["import_destination"] = (
            capo_sesv2.types.import_destination.deserialize_json(
                data["ImportDestination"]
            )
        )
    else:
        raise DeserializationError("CreateImportJobRequest.import_destination required")
    if "ImportDataSource" in data:
        import capo_sesv2.types.import_data_source

        out["import_data_source"] = (
            capo_sesv2.types.import_data_source.deserialize_json(
                data["ImportDataSource"]
            )
        )
    else:
        raise DeserializationError("CreateImportJobRequest.import_data_source required")
    return out
