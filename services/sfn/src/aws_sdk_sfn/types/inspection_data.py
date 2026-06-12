"""Generated from Smithy shape ``com.amazonaws.sfn#InspectionData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sfn.types.inspection_data_request
    import aws_sdk_sfn.types.inspection_data_response
    import aws_sdk_sfn.types.inspection_error_details
    import aws_sdk_sfn.types.inspection_max_concurrency
    import aws_sdk_sfn.types.inspection_tolerated_failure_count
    import aws_sdk_sfn.types.inspection_tolerated_failure_percentage
    import aws_sdk_sfn.types.sensitive_data


class InspectionData(TypedDict):
    input: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The raw state input.</p>"""
    after_arguments: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The input after Step Functions applies an Arguments filter. This event will only be present when QueryLanguage for the state machine or individual states is set to JSONata. For more info, see <a href=\"https://docs.aws.amazon.com/step-functions/latest/dg/data-transform.html\">Transforming data with Step Functions</a>.</p>"""
    after_input_path: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The input after Step Functions applies the <a href=\"https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-inputpath\">InputPath</a> filter. Not populated when QueryLanguage is JSONata.</p>"""
    after_parameters: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The effective input after Step Functions applies the <a href=\"https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-parameters\">Parameters</a> filter. Not populated when QueryLanguage is JSONata.</p>"""
    result: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The state's raw result.</p>"""
    after_result_selector: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The effective result after Step Functions applies the <a href=\"https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector\">ResultSelector</a> filter. Not populated when QueryLanguage is JSONata.</p>"""
    after_result_path: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The effective result combined with the raw state input after Step Functions applies the <a href=\"https://docs.aws.amazon.com/step-functions/latest/dg/input-output-resultpath.html\">ResultPath</a> filter. Not populated when QueryLanguage is JSONata.</p>"""
    request: NotRequired[
        "aws_sdk_sfn.types.inspection_data_request.InspectionDataRequest"
    ]
    """<p>The raw HTTP request that is sent when you test an HTTP Task.</p>"""
    response: NotRequired[
        "aws_sdk_sfn.types.inspection_data_response.InspectionDataResponse"
    ]
    """<p>The raw HTTP response that is returned when you test an HTTP Task.</p>"""
    variables: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>JSON string that contains the set of workflow variables after execution of the state. The set will include variables assigned in the state and variables set up as test state input.</p>"""
    error_details: NotRequired[
        "aws_sdk_sfn.types.inspection_error_details.InspectionErrorDetails"
    ]
    """<p>An object containing data about a handled exception in the tested state.</p>"""
    after_items_path: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The effective input after the ItemsPath filter is applied. Not populated when the QueryLanguage is JSONata.</p>"""
    after_item_selector: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>An array containing the inputs for each Map iteration, transformed by the ItemSelector specified in a Map state.</p>"""
    after_item_batcher: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The effective input after the ItemBatcher filter is applied in a Map state.</p>"""
    after_items_pointer: NotRequired["aws_sdk_sfn.types.sensitive_data.SensitiveData"]
    """<p>The effective input after the ItemsPointer filter is applied in a Map state.</p>"""
    tolerated_failure_count: NotRequired[
        "aws_sdk_sfn.types.inspection_tolerated_failure_count.InspectionToleratedFailureCount"
    ]
    """<p>The tolerated failure threshold for a Map state as defined in number of Map state iterations.</p>"""
    tolerated_failure_percentage: NotRequired[
        "aws_sdk_sfn.types.inspection_tolerated_failure_percentage.InspectionToleratedFailurePercentage"
    ]
    """<p>The tolerated failure threshold for a Map state as defined in percentage of Map state iterations.</p>"""
    max_concurrency: NotRequired[
        "aws_sdk_sfn.types.inspection_max_concurrency.InspectionMaxConcurrency"
    ]
    """<p>The max concurrency of the Map state.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InspectionData) -> dict:
    out: dict = {}
    if "input" in value:
        out["input"] = value["input"]
    if "after_arguments" in value:
        out["afterArguments"] = value["after_arguments"]
    if "after_input_path" in value:
        out["afterInputPath"] = value["after_input_path"]
    if "after_parameters" in value:
        out["afterParameters"] = value["after_parameters"]
    if "result" in value:
        out["result"] = value["result"]
    if "after_result_selector" in value:
        out["afterResultSelector"] = value["after_result_selector"]
    if "after_result_path" in value:
        out["afterResultPath"] = value["after_result_path"]
    if "request" in value:
        import aws_sdk_sfn.types.inspection_data_request

        out["request"] = (
            aws_sdk_sfn.types.inspection_data_request.serialize_aws_json_1_0(
                value["request"]
            )
        )
    if "response" in value:
        import aws_sdk_sfn.types.inspection_data_response

        out["response"] = (
            aws_sdk_sfn.types.inspection_data_response.serialize_aws_json_1_0(
                value["response"]
            )
        )
    if "variables" in value:
        out["variables"] = value["variables"]
    if "error_details" in value:
        import aws_sdk_sfn.types.inspection_error_details

        out["errorDetails"] = (
            aws_sdk_sfn.types.inspection_error_details.serialize_aws_json_1_0(
                value["error_details"]
            )
        )
    if "after_items_path" in value:
        out["afterItemsPath"] = value["after_items_path"]
    if "after_item_selector" in value:
        out["afterItemSelector"] = value["after_item_selector"]
    if "after_item_batcher" in value:
        out["afterItemBatcher"] = value["after_item_batcher"]
    if "after_items_pointer" in value:
        out["afterItemsPointer"] = value["after_items_pointer"]
    if "tolerated_failure_count" in value:
        out["toleratedFailureCount"] = value["tolerated_failure_count"]
    if "tolerated_failure_percentage" in value:
        out["toleratedFailurePercentage"] = value["tolerated_failure_percentage"]
    if "max_concurrency" in value:
        out["maxConcurrency"] = value["max_concurrency"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InspectionData:
    out: InspectionData = {}  # type: ignore[typeddict-item]
    if "input" in data:
        out["input"] = data["input"]
    if "afterArguments" in data:
        out["after_arguments"] = data["afterArguments"]
    if "afterInputPath" in data:
        out["after_input_path"] = data["afterInputPath"]
    if "afterParameters" in data:
        out["after_parameters"] = data["afterParameters"]
    if "result" in data:
        out["result"] = data["result"]
    if "afterResultSelector" in data:
        out["after_result_selector"] = data["afterResultSelector"]
    if "afterResultPath" in data:
        out["after_result_path"] = data["afterResultPath"]
    if "request" in data:
        import aws_sdk_sfn.types.inspection_data_request

        out["request"] = (
            aws_sdk_sfn.types.inspection_data_request.deserialize_aws_json_1_0(
                data["request"]
            )
        )
    if "response" in data:
        import aws_sdk_sfn.types.inspection_data_response

        out["response"] = (
            aws_sdk_sfn.types.inspection_data_response.deserialize_aws_json_1_0(
                data["response"]
            )
        )
    if "variables" in data:
        out["variables"] = data["variables"]
    if "errorDetails" in data:
        import aws_sdk_sfn.types.inspection_error_details

        out["error_details"] = (
            aws_sdk_sfn.types.inspection_error_details.deserialize_aws_json_1_0(
                data["errorDetails"]
            )
        )
    if "afterItemsPath" in data:
        out["after_items_path"] = data["afterItemsPath"]
    if "afterItemSelector" in data:
        out["after_item_selector"] = data["afterItemSelector"]
    if "afterItemBatcher" in data:
        out["after_item_batcher"] = data["afterItemBatcher"]
    if "afterItemsPointer" in data:
        out["after_items_pointer"] = data["afterItemsPointer"]
    if "toleratedFailureCount" in data:
        out["tolerated_failure_count"] = data["toleratedFailureCount"]
    if "toleratedFailurePercentage" in data:
        out["tolerated_failure_percentage"] = data["toleratedFailurePercentage"]
    if "maxConcurrency" in data:
        out["max_concurrency"] = data["maxConcurrency"]
    return out
