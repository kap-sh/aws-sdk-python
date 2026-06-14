"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftSelfGrantStatusOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.self_grant_status_details


class RedshiftSelfGrantStatusOutput(TypedDict):
    self_grant_status_details: (
        "aws_sdk_datazone.types.self_grant_status_details.SelfGrantStatusDetails"
    )
    """<p>The details for the self granting status for an Amazon Redshift data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftSelfGrantStatusOutput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.self_grant_status_details

    out["selfGrantStatusDetails"] = (
        aws_sdk_datazone.types.self_grant_status_details.serialize_json(
            value["self_grant_status_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> RedshiftSelfGrantStatusOutput:
    out: RedshiftSelfGrantStatusOutput = {}  # type: ignore[typeddict-item]
    if "selfGrantStatusDetails" in data:
        import aws_sdk_datazone.types.self_grant_status_details

        out["self_grant_status_details"] = (
            aws_sdk_datazone.types.self_grant_status_details.deserialize_json(
                data["selfGrantStatusDetails"]
            )
        )
    else:
        raise DeserializationError(
            "RedshiftSelfGrantStatusOutput.self_grant_status_details required"
        )
    return out
