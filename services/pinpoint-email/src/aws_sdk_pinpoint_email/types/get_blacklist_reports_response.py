"""Generated from Smithy shape ``com.amazonaws.pinpointemail#GetBlacklistReportsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.blacklist_report


class GetBlacklistReportsResponse(TypedDict):
    blacklist_report: "aws_sdk_pinpoint_email.types.blacklist_report.BlacklistReport"
    """<p>An object that contains information about a blacklist that one of your dedicated IP addresses appears on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBlacklistReportsResponse) -> dict:
    out: dict = {}
    import aws_sdk_pinpoint_email.types.blacklist_report

    out["BlacklistReport"] = (
        aws_sdk_pinpoint_email.types.blacklist_report.serialize_json(
            value["blacklist_report"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetBlacklistReportsResponse:
    out: GetBlacklistReportsResponse = {}  # type: ignore[typeddict-item]
    if "BlacklistReport" in data:
        import aws_sdk_pinpoint_email.types.blacklist_report

        out["blacklist_report"] = (
            aws_sdk_pinpoint_email.types.blacklist_report.deserialize_json(
                data["BlacklistReport"]
            )
        )
    else:
        raise DeserializationError(
            "GetBlacklistReportsResponse.blacklist_report required"
        )
    return out
