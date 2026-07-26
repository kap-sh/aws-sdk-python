"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeRemediationExceptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.remediation_exceptions
    import capo_config_service.types.string


class DescribeRemediationExceptionsResponse(TypedDict, closed=True):
    remediation_exceptions: NotRequired[
        "capo_config_service.types.remediation_exceptions.RemediationExceptions"
    ]
    """<p>Returns a list of remediation exception objects.</p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRemediationExceptionsResponse) -> dict:
    out: dict = {}
    if "remediation_exceptions" in value:
        import capo_config_service.types.remediation_exceptions

        out["RemediationExceptions"] = (
            capo_config_service.types.remediation_exceptions.serialize_aws_json_1_1(
                value["remediation_exceptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRemediationExceptionsResponse:
    out: DescribeRemediationExceptionsResponse = {}  # type: ignore[typeddict-item]
    if "RemediationExceptions" in data:
        import capo_config_service.types.remediation_exceptions

        out["remediation_exceptions"] = (
            capo_config_service.types.remediation_exceptions.deserialize_aws_json_1_1(
                data["RemediationExceptions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
