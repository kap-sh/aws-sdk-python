"""Generated from Smithy shape ``com.amazonaws.support#DescribeTrustedAdvisorCheckSummariesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.string_list


class DescribeTrustedAdvisorCheckSummariesRequest(TypedDict):
    check_ids: "aws_sdk_support.types.string_list.StringList"
    """<p>The IDs of the Trusted Advisor checks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrustedAdvisorCheckSummariesRequest) -> dict:
    out: dict = {}
    import aws_sdk_support.types.string_list

    out["checkIds"] = aws_sdk_support.types.string_list.serialize_aws_json_1_1(
        value["check_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrustedAdvisorCheckSummariesRequest:
    out: DescribeTrustedAdvisorCheckSummariesRequest = {}  # type: ignore[typeddict-item]
    if "checkIds" in data:
        import aws_sdk_support.types.string_list

        out["check_ids"] = aws_sdk_support.types.string_list.deserialize_aws_json_1_1(
            data["checkIds"]
        )
    else:
        raise DeserializationError(
            "DescribeTrustedAdvisorCheckSummariesRequest.check_ids required"
        )
    return out
