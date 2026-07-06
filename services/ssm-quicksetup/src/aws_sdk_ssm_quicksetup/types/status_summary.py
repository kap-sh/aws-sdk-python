"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#StatusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_quicksetup.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_quicksetup.types.status
    import aws_sdk_ssm_quicksetup.types.status_details
    import aws_sdk_ssm_quicksetup.types.status_type


class StatusSummary(TypedDict, closed=True):
    status_type: "aws_sdk_ssm_quicksetup.types.status_type.StatusType"
    """<p>The type of a status summary.</p>"""
    status: NotRequired["aws_sdk_ssm_quicksetup.types.status.Status"]
    """<p>The current status.</p>"""
    status_message: NotRequired["str"]
    """<p>When applicable, returns an informational message relevant to the current status and status type of the status summary object. We don't recommend implementing parsing logic around this value since the messages returned can vary in format.</p>"""
    last_updated_at: "datetime.datetime"
    """<p>The datetime stamp when the status was last updated.</p>"""
    status_details: NotRequired[
        "aws_sdk_ssm_quicksetup.types.status_details.StatusDetails"
    ]
    """<p>Details about the status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatusSummary) -> dict:
    out: dict = {}
    import aws_sdk_ssm_quicksetup.types.status_type

    out["StatusType"] = aws_sdk_ssm_quicksetup.types.status_type.serialize_json(
        value["status_type"]
    )
    if "status" in value:
        import aws_sdk_ssm_quicksetup.types.status

        out["Status"] = aws_sdk_ssm_quicksetup.types.status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    import aws_sdk_ssm_quicksetup.types._prelude.timestamp

    out["LastUpdatedAt"] = (
        aws_sdk_ssm_quicksetup.types._prelude.timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    if "status_details" in value:
        import aws_sdk_ssm_quicksetup.types.status_details

        out["StatusDetails"] = (
            aws_sdk_ssm_quicksetup.types.status_details.serialize_json(
                value["status_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> StatusSummary:
    out: StatusSummary = {}  # type: ignore[typeddict-item]
    if "StatusType" in data:
        import aws_sdk_ssm_quicksetup.types.status_type

        out["status_type"] = aws_sdk_ssm_quicksetup.types.status_type.deserialize_json(
            data["StatusType"]
        )
    else:
        raise DeserializationError("StatusSummary.status_type required")
    if "Status" in data:
        import aws_sdk_ssm_quicksetup.types.status

        out["status"] = aws_sdk_ssm_quicksetup.types.status.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "LastUpdatedAt" in data:
        import aws_sdk_ssm_quicksetup.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_ssm_quicksetup.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("StatusSummary.last_updated_at required")
    if "StatusDetails" in data:
        import aws_sdk_ssm_quicksetup.types.status_details

        out["status_details"] = (
            aws_sdk_ssm_quicksetup.types.status_details.deserialize_json(
                data["StatusDetails"]
            )
        )
    return out
