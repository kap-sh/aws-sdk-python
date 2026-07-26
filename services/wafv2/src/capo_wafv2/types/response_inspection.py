"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseInspection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.response_inspection_body_contains
    import capo_wafv2.types.response_inspection_header
    import capo_wafv2.types.response_inspection_json
    import capo_wafv2.types.response_inspection_status_code


class ResponseInspection(TypedDict, closed=True):
    status_code: NotRequired[
        "capo_wafv2.types.response_inspection_status_code.ResponseInspectionStatusCode"
    ]
    """<p>Configures inspection of the response status code for success and failure indicators. </p>"""
    header: NotRequired[
        "capo_wafv2.types.response_inspection_header.ResponseInspectionHeader"
    ]
    """<p>Configures inspection of the response header for success and failure indicators. </p>"""
    body_contains: NotRequired[
        "capo_wafv2.types.response_inspection_body_contains.ResponseInspectionBodyContains"
    ]
    """<p>Configures inspection of the response body for success and failure indicators. WAF can inspect the first 65,536 bytes (64 KB) of the response body. </p>"""
    json: NotRequired[
        "capo_wafv2.types.response_inspection_json.ResponseInspectionJson"
    ]
    """<p>Configures inspection of the response JSON for success and failure indicators. WAF can inspect the first 65,536 bytes (64 KB) of the response JSON. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseInspection) -> dict:
    out: dict = {}
    if "status_code" in value:
        import capo_wafv2.types.response_inspection_status_code

        out["StatusCode"] = (
            capo_wafv2.types.response_inspection_status_code.serialize_aws_json_1_1(
                value["status_code"]
            )
        )
    if "header" in value:
        import capo_wafv2.types.response_inspection_header

        out["Header"] = (
            capo_wafv2.types.response_inspection_header.serialize_aws_json_1_1(
                value["header"]
            )
        )
    if "body_contains" in value:
        import capo_wafv2.types.response_inspection_body_contains

        out["BodyContains"] = (
            capo_wafv2.types.response_inspection_body_contains.serialize_aws_json_1_1(
                value["body_contains"]
            )
        )
    if "json" in value:
        import capo_wafv2.types.response_inspection_json

        out["Json"] = capo_wafv2.types.response_inspection_json.serialize_aws_json_1_1(
            value["json"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseInspection:
    out: ResponseInspection = {}  # type: ignore[typeddict-item]
    if "StatusCode" in data:
        import capo_wafv2.types.response_inspection_status_code

        out["status_code"] = (
            capo_wafv2.types.response_inspection_status_code.deserialize_aws_json_1_1(
                data["StatusCode"]
            )
        )
    if "Header" in data:
        import capo_wafv2.types.response_inspection_header

        out["header"] = (
            capo_wafv2.types.response_inspection_header.deserialize_aws_json_1_1(
                data["Header"]
            )
        )
    if "BodyContains" in data:
        import capo_wafv2.types.response_inspection_body_contains

        out["body_contains"] = (
            capo_wafv2.types.response_inspection_body_contains.deserialize_aws_json_1_1(
                data["BodyContains"]
            )
        )
    if "Json" in data:
        import capo_wafv2.types.response_inspection_json

        out["json"] = (
            capo_wafv2.types.response_inspection_json.deserialize_aws_json_1_1(
                data["Json"]
            )
        )
    return out
