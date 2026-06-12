"""Generated from Smithy shape ``com.amazonaws.appstream#FleetError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.fleet_error_code
    import aws_sdk_appstream.types.string


class FleetError(TypedDict):
    error_code: NotRequired["aws_sdk_appstream.types.fleet_error_code.FleetErrorCode"]
    """<p>The error code.</p>"""
    error_message: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import aws_sdk_appstream.types.fleet_error_code

        out["ErrorCode"] = (
            aws_sdk_appstream.types.fleet_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FleetError:
    out: FleetError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        import aws_sdk_appstream.types.fleet_error_code

        out["error_code"] = (
            aws_sdk_appstream.types.fleet_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
