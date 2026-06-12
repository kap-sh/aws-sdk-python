"""Generated from Smithy shape ``com.amazonaws.support#RefreshTrustedAdvisorCheckResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.trusted_advisor_check_refresh_status


class RefreshTrustedAdvisorCheckResponse(TypedDict):
    status: "aws_sdk_support.types.trusted_advisor_check_refresh_status.TrustedAdvisorCheckRefreshStatus"
    """<p>The current refresh status for a check, including the amount of time until the check is eligible for refresh.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshTrustedAdvisorCheckResponse) -> dict:
    out: dict = {}
    import aws_sdk_support.types.trusted_advisor_check_refresh_status

    out["status"] = (
        aws_sdk_support.types.trusted_advisor_check_refresh_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RefreshTrustedAdvisorCheckResponse:
    out: RefreshTrustedAdvisorCheckResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_support.types.trusted_advisor_check_refresh_status

        out["status"] = (
            aws_sdk_support.types.trusted_advisor_check_refresh_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError("RefreshTrustedAdvisorCheckResponse.status required")
    return out
