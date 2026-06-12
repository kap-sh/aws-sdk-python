"""Generated from Smithy shape ``com.amazonaws.support#DescribeServicesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_support.types.language
    import aws_sdk_support.types.service_code_list


class DescribeServicesRequest(TypedDict):
    service_code_list: NotRequired[
        "aws_sdk_support.types.service_code_list.ServiceCodeList"
    ]
    """<p>A JSON-formatted list of service codes available for Amazon Web Services services.</p>"""
    language: NotRequired["aws_sdk_support.types.language.Language"]
    """<p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English (\"en\"), Japanese (\"ja\") and Korean (“ko”). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServicesRequest) -> dict:
    out: dict = {}
    if "service_code_list" in value:
        import aws_sdk_support.types.service_code_list

        out["serviceCodeList"] = (
            aws_sdk_support.types.service_code_list.serialize_aws_json_1_1(
                value["service_code_list"]
            )
        )
    if "language" in value:
        out["language"] = value["language"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServicesRequest:
    out: DescribeServicesRequest = {}  # type: ignore[typeddict-item]
    if "serviceCodeList" in data:
        import aws_sdk_support.types.service_code_list

        out["service_code_list"] = (
            aws_sdk_support.types.service_code_list.deserialize_aws_json_1_1(
                data["serviceCodeList"]
            )
        )
    if "language" in data:
        out["language"] = data["language"]
    return out
