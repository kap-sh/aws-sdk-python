"""Generated from Smithy shape ``com.amazonaws.support#DescribeTrustedAdvisorCheckRefreshStatusesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.string_list


class DescribeTrustedAdvisorCheckRefreshStatusesRequest(TypedDict):
    check_ids: "aws_sdk_support.types.string_list.StringList"
    """<p>The IDs of the Trusted Advisor checks to get the status.</p> <note> <p>If you specify the check ID of a check that is automatically refreshed, you might see an <code>InvalidParameterValue</code> error.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeTrustedAdvisorCheckRefreshStatusesRequest,
) -> dict:
    out: dict = {}
    import aws_sdk_support.types.string_list

    out["checkIds"] = aws_sdk_support.types.string_list.serialize_aws_json_1_1(
        value["check_ids"]
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeTrustedAdvisorCheckRefreshStatusesRequest:
    out: DescribeTrustedAdvisorCheckRefreshStatusesRequest = {}  # type: ignore[typeddict-item]
    if "checkIds" in data:
        import aws_sdk_support.types.string_list

        out["check_ids"] = aws_sdk_support.types.string_list.deserialize_aws_json_1_1(
            data["checkIds"]
        )
    else:
        raise DeserializationError(
            "DescribeTrustedAdvisorCheckRefreshStatusesRequest.check_ids required"
        )
    return out
