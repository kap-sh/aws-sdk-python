"""Generated from Smithy shape ``com.amazonaws.support#DescribeCreateCaseOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.category_code
    import aws_sdk_support.types.issue_type
    import aws_sdk_support.types.language
    import aws_sdk_support.types.service_code2


class DescribeCreateCaseOptionsRequest(TypedDict):
    issue_type: "aws_sdk_support.types.issue_type.IssueType"
    """<p>The type of issue for the case. You can specify <code>customer-service</code> or <code>technical</code>. If you don't specify a value, the default is <code>technical</code>.</p>"""
    service_code: "aws_sdk_support.types.service_code2.ServiceCode2"
    """<p>The code for the Amazon Web Services service. You can use the <a>DescribeServices</a> operation to get the possible <code>serviceCode</code> values.</p>"""
    language: "aws_sdk_support.types.language.Language"
    r"""<p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English (\"en\"), Japanese (\"ja\") and Korean (“ko”). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>"""
    category_code: "aws_sdk_support.types.category_code.CategoryCode"
    """<p>The category of problem for the support case. You also use the <a>DescribeServices</a> operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCreateCaseOptionsRequest) -> dict:
    out: dict = {}
    out["issueType"] = value["issue_type"]
    out["serviceCode"] = value["service_code"]
    out["language"] = value["language"]
    out["categoryCode"] = value["category_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCreateCaseOptionsRequest:
    out: DescribeCreateCaseOptionsRequest = {}  # type: ignore[typeddict-item]
    if "issueType" in data:
        out["issue_type"] = data["issueType"]
    else:
        raise DeserializationError(
            "DescribeCreateCaseOptionsRequest.issue_type required"
        )
    if "serviceCode" in data:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError(
            "DescribeCreateCaseOptionsRequest.service_code required"
        )
    if "language" in data:
        out["language"] = data["language"]
    else:
        raise DeserializationError("DescribeCreateCaseOptionsRequest.language required")
    if "categoryCode" in data:
        out["category_code"] = data["categoryCode"]
    else:
        raise DeserializationError(
            "DescribeCreateCaseOptionsRequest.category_code required"
        )
    return out
