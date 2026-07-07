"""Generated from Smithy shape ``com.amazonaws.support#DescribeTrustedAdvisorCheckRefreshStatusesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.trusted_advisor_check_refresh_status_list


class DescribeTrustedAdvisorCheckRefreshStatusesResponse(TypedDict, closed=True):
    statuses: "aws_sdk_support.types.trusted_advisor_check_refresh_status_list.TrustedAdvisorCheckRefreshStatusList"
    """<p>The refresh status of the specified Trusted Advisor checks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeTrustedAdvisorCheckRefreshStatusesResponse,
) -> dict:
    out: dict = {}
    import aws_sdk_support.types.trusted_advisor_check_refresh_status_list

    out["statuses"] = (
        aws_sdk_support.types.trusted_advisor_check_refresh_status_list.serialize_aws_json_1_1(
            value["statuses"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeTrustedAdvisorCheckRefreshStatusesResponse:
    out: DescribeTrustedAdvisorCheckRefreshStatusesResponse = {}  # type: ignore[typeddict-item]
    if "statuses" in data:
        import aws_sdk_support.types.trusted_advisor_check_refresh_status_list

        out["statuses"] = (
            aws_sdk_support.types.trusted_advisor_check_refresh_status_list.deserialize_aws_json_1_1(
                data["statuses"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeTrustedAdvisorCheckRefreshStatusesResponse.statuses required"
        )
    return out
