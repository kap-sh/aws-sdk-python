"""Generated from Smithy shape ``com.amazonaws.qapps#ExportQAppSessionDataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.q_apps_timestamp


class ExportQAppSessionDataOutput(TypedDict, closed=True):
    csv_file_link: "str"
    """<p>The link where the exported Q App session data can be downloaded from.</p>"""
    expires_at: "capo_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time when the link for the exported Q App session data expires.</p>"""
    session_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the Q App data collection session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportQAppSessionDataOutput) -> dict:
    out: dict = {}
    out["csvFileLink"] = value["csv_file_link"]
    import capo_qapps.types.q_apps_timestamp

    out["expiresAt"] = capo_qapps.types.q_apps_timestamp.serialize_json(
        value["expires_at"]
    )
    out["sessionArn"] = value["session_arn"]
    return out


def deserialize_json(data: dict) -> ExportQAppSessionDataOutput:
    out: ExportQAppSessionDataOutput = {}  # type: ignore[typeddict-item]
    if "csvFileLink" in data:
        out["csv_file_link"] = data["csvFileLink"]
    else:
        raise DeserializationError("ExportQAppSessionDataOutput.csv_file_link required")
    if "expiresAt" in data:
        import capo_qapps.types.q_apps_timestamp

        out["expires_at"] = capo_qapps.types.q_apps_timestamp.deserialize_json(
            data["expiresAt"]
        )
    else:
        raise DeserializationError("ExportQAppSessionDataOutput.expires_at required")
    if "sessionArn" in data:
        out["session_arn"] = data["sessionArn"]
    else:
        raise DeserializationError("ExportQAppSessionDataOutput.session_arn required")
    return out
