"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseInspection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.response_inspection_body_contains
    import aws_sdk_wafv2.types.response_inspection_header
    import aws_sdk_wafv2.types.response_inspection_json
    import aws_sdk_wafv2.types.response_inspection_status_code


class ResponseInspection(TypedDict, closed=True):
    status_code: NotRequired[
        "aws_sdk_wafv2.types.response_inspection_status_code.ResponseInspectionStatusCode"
    ]
    """<p>Configures inspection of the response status code for success and failure indicators. </p>"""
    header: NotRequired[
        "aws_sdk_wafv2.types.response_inspection_header.ResponseInspectionHeader"
    ]
    """<p>Configures inspection of the response header for success and failure indicators. </p>"""
    body_contains: NotRequired[
        "aws_sdk_wafv2.types.response_inspection_body_contains.ResponseInspectionBodyContains"
    ]
    """<p>Configures inspection of the response body for success and failure indicators. WAF can inspect the first 65,536 bytes (64 KB) of the response body. </p>"""
    json: NotRequired[
        "aws_sdk_wafv2.types.response_inspection_json.ResponseInspectionJson"
    ]
    """<p>Configures inspection of the response JSON for success and failure indicators. WAF can inspect the first 65,536 bytes (64 KB) of the response JSON. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseInspection) -> dict:
    out: dict = {}
    if "status_code" in value:
        import aws_sdk_wafv2.types.response_inspection_status_code

        out["StatusCode"] = (
            aws_sdk_wafv2.types.response_inspection_status_code.serialize_aws_json_1_1(
                value["status_code"]
            )
        )
    if "header" in value:
        import aws_sdk_wafv2.types.response_inspection_header

        out["Header"] = (
            aws_sdk_wafv2.types.response_inspection_header.serialize_aws_json_1_1(
                value["header"]
            )
        )
    if "body_contains" in value:
        import aws_sdk_wafv2.types.response_inspection_body_contains

        out["BodyContains"] = (
            aws_sdk_wafv2.types.response_inspection_body_contains.serialize_aws_json_1_1(
                value["body_contains"]
            )
        )
    if "json" in value:
        import aws_sdk_wafv2.types.response_inspection_json

        out["Json"] = (
            aws_sdk_wafv2.types.response_inspection_json.serialize_aws_json_1_1(
                value["json"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseInspection:
    out: ResponseInspection = {}  # type: ignore[typeddict-item]
    if "StatusCode" in data:
        import aws_sdk_wafv2.types.response_inspection_status_code

        out["status_code"] = (
            aws_sdk_wafv2.types.response_inspection_status_code.deserialize_aws_json_1_1(
                data["StatusCode"]
            )
        )
    if "Header" in data:
        import aws_sdk_wafv2.types.response_inspection_header

        out["header"] = (
            aws_sdk_wafv2.types.response_inspection_header.deserialize_aws_json_1_1(
                data["Header"]
            )
        )
    if "BodyContains" in data:
        import aws_sdk_wafv2.types.response_inspection_body_contains

        out["body_contains"] = (
            aws_sdk_wafv2.types.response_inspection_body_contains.deserialize_aws_json_1_1(
                data["BodyContains"]
            )
        )
    if "Json" in data:
        import aws_sdk_wafv2.types.response_inspection_json

        out["json"] = (
            aws_sdk_wafv2.types.response_inspection_json.deserialize_aws_json_1_1(
                data["Json"]
            )
        )
    return out
