"""Generated from Smithy shape ``com.amazonaws.ssmincidents#Finding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_incidents.types.finding_details
    import aws_sdk_ssm_incidents.types.finding_id


class Finding(TypedDict, closed=True):
    id: "aws_sdk_ssm_incidents.types.finding_id.FindingId"
    """<p>The ID assigned to the finding.</p>"""
    creation_time: "datetime.datetime"
    """<p>The timestamp for when a finding was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp for when the finding was most recently updated with additional information.</p>"""
    details: NotRequired["aws_sdk_ssm_incidents.types.finding_details.FindingDetails"]
    """<p>Details about the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Finding) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_ssm_incidents.types._prelude.timestamp

    out["creationTime"] = aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    import aws_sdk_ssm_incidents.types._prelude.timestamp

    out["lastModifiedTime"] = (
        aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["last_modified_time"]
        )
    )
    if "details" in value:
        import aws_sdk_ssm_incidents.types.finding_details

        out["details"] = aws_sdk_ssm_incidents.types.finding_details.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Finding.id required")
    if "creationTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("Finding.creation_time required")
    if "lastModifiedTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("Finding.last_modified_time required")
    if "details" in data:
        import aws_sdk_ssm_incidents.types.finding_details

        out["details"] = aws_sdk_ssm_incidents.types.finding_details.deserialize_json(
            data["details"]
        )
    return out
