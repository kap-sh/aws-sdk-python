"""Generated from Smithy shape ``com.amazonaws.sesv2#ExportDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.data_format
    import capo_sesv2.types.s3_url


class ExportDestination(TypedDict, closed=True):
    data_format: "capo_sesv2.types.data_format.DataFormat"
    """<p>The data format of the final export job file, can be one of the following:</p> <ul> <li> <p> <code>CSV</code> - A comma-separated values file.</p> </li> <li> <p> <code>JSON</code> - A Json file.</p> </li> </ul>"""
    s3_url: NotRequired["capo_sesv2.types.s3_url.S3Url"]
    """<p>An Amazon S3 pre-signed URL that points to the generated export file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportDestination) -> dict:
    out: dict = {}
    import capo_sesv2.types.data_format

    out["DataFormat"] = capo_sesv2.types.data_format.serialize_json(
        value["data_format"]
    )
    if "s3_url" in value:
        out["S3Url"] = value["s3_url"]
    return out


def deserialize_json(data: dict) -> ExportDestination:
    out: ExportDestination = {}  # type: ignore[typeddict-item]
    if "DataFormat" in data:
        import capo_sesv2.types.data_format

        out["data_format"] = capo_sesv2.types.data_format.deserialize_json(
            data["DataFormat"]
        )
    else:
        raise DeserializationError("ExportDestination.data_format required")
    if "S3Url" in data:
        out["s3_url"] = data["S3Url"]
    return out
