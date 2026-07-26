"""Generated from Smithy shape ``com.amazonaws.support#RefreshTrustedAdvisorCheckResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_support.errors import DeserializationError

if TYPE_CHECKING:
    import capo_support.types.trusted_advisor_check_refresh_status


class RefreshTrustedAdvisorCheckResponse(TypedDict, closed=True):
    status: "capo_support.types.trusted_advisor_check_refresh_status.TrustedAdvisorCheckRefreshStatus"
    """<p>The current refresh status for a check, including the amount of time until the check is eligible for refresh.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshTrustedAdvisorCheckResponse) -> dict:
    out: dict = {}
    import capo_support.types.trusted_advisor_check_refresh_status

    out["status"] = (
        capo_support.types.trusted_advisor_check_refresh_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RefreshTrustedAdvisorCheckResponse:
    out: RefreshTrustedAdvisorCheckResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_support.types.trusted_advisor_check_refresh_status

        out["status"] = (
            capo_support.types.trusted_advisor_check_refresh_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError("RefreshTrustedAdvisorCheckResponse.status required")
    return out
