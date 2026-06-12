"""Generated from Smithy shape ``com.amazonaws.support#DescribeSupportedLanguagesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.validated_category_code
    import aws_sdk_support.types.validated_issue_type_string
    import aws_sdk_support.types.validated_service_code


class DescribeSupportedLanguagesRequest(TypedDict):
    issue_type: (
        "aws_sdk_support.types.validated_issue_type_string.ValidatedIssueTypeString"
    )
    """<p>The type of issue for the case. You can specify <code>customer-service</code> or <code>technical</code>.</p>"""
    service_code: "aws_sdk_support.types.validated_service_code.ValidatedServiceCode"
    """<p>The code for the Amazon Web Services service. You can use the <a>DescribeServices</a> operation to get the possible <code>serviceCode</code> values.</p>"""
    category_code: "aws_sdk_support.types.validated_category_code.ValidatedCategoryCode"
    """<p>The category of problem for the support case. You also use the <a>DescribeServices</a> operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSupportedLanguagesRequest) -> dict:
    out: dict = {}
    out["issueType"] = value["issue_type"]
    out["serviceCode"] = value["service_code"]
    out["categoryCode"] = value["category_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSupportedLanguagesRequest:
    out: DescribeSupportedLanguagesRequest = {}  # type: ignore[typeddict-item]
    if "issueType" in data:
        out["issue_type"] = data["issueType"]
    else:
        raise DeserializationError(
            "DescribeSupportedLanguagesRequest.issue_type required"
        )
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError(
            "DescribeSupportedLanguagesRequest.service_code required"
        )
    if "categoryCode" in data:
        out["category_code"] = data["categoryCode"]
    else:
        raise DeserializationError(
            "DescribeSupportedLanguagesRequest.category_code required"
        )
    return out
