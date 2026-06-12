"""Generated from Smithy shape ``com.amazonaws.support#DescribeTrustedAdvisorChecksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.trusted_advisor_check_list


class DescribeTrustedAdvisorChecksResponse(TypedDict):
    checks: "aws_sdk_support.types.trusted_advisor_check_list.TrustedAdvisorCheckList"
    """<p>Information about all available Trusted Advisor checks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrustedAdvisorChecksResponse) -> dict:
    out: dict = {}
    import aws_sdk_support.types.trusted_advisor_check_list

    out["checks"] = (
        aws_sdk_support.types.trusted_advisor_check_list.serialize_aws_json_1_1(
            value["checks"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrustedAdvisorChecksResponse:
    out: DescribeTrustedAdvisorChecksResponse = {}  # type: ignore[typeddict-item]
    if "checks" in data:
        import aws_sdk_support.types.trusted_advisor_check_list

        out["checks"] = (
            aws_sdk_support.types.trusted_advisor_check_list.deserialize_aws_json_1_1(
                data["checks"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeTrustedAdvisorChecksResponse.checks required"
        )
    return out
