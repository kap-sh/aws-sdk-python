"""Generated from Smithy shape ``com.amazonaws.eventbridge#HttpParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.header_parameters_map
    import aws_sdk_eventbridge.types.path_parameter_list
    import aws_sdk_eventbridge.types.query_string_parameters_map


class HttpParameters(TypedDict):
    path_parameter_values: NotRequired[
        "aws_sdk_eventbridge.types.path_parameter_list.PathParameterList"
    ]
    r"""<p>The path parameter values to be used to populate API Gateway API or EventBridge ApiDestination path wildcards (\"*\").</p>"""
    header_parameters: NotRequired[
        "aws_sdk_eventbridge.types.header_parameters_map.HeaderParametersMap"
    ]
    """<p>The headers that need to be sent as part of request invoking the API Gateway API or EventBridge ApiDestination.</p>"""
    query_string_parameters: NotRequired[
        "aws_sdk_eventbridge.types.query_string_parameters_map.QueryStringParametersMap"
    ]
    """<p>The query string keys/values that need to be sent as part of request invoking the API Gateway API or EventBridge ApiDestination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpParameters) -> dict:
    out: dict = {}
    if "path_parameter_values" in value:
        import aws_sdk_eventbridge.types.path_parameter_list

        out["PathParameterValues"] = (
            aws_sdk_eventbridge.types.path_parameter_list.serialize_aws_json_1_1(
                value["path_parameter_values"]
            )
        )
    if "header_parameters" in value:
        import aws_sdk_eventbridge.types.header_parameters_map

        out["HeaderParameters"] = (
            aws_sdk_eventbridge.types.header_parameters_map.serialize_aws_json_1_1(
                value["header_parameters"]
            )
        )
    if "query_string_parameters" in value:
        import aws_sdk_eventbridge.types.query_string_parameters_map

        out["QueryStringParameters"] = (
            aws_sdk_eventbridge.types.query_string_parameters_map.serialize_aws_json_1_1(
                value["query_string_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpParameters:
    out: HttpParameters = {}  # type: ignore[typeddict-item]
    if "PathParameterValues" in data:
        import aws_sdk_eventbridge.types.path_parameter_list

        out["path_parameter_values"] = (
            aws_sdk_eventbridge.types.path_parameter_list.deserialize_aws_json_1_1(
                data["PathParameterValues"]
            )
        )
    if "HeaderParameters" in data:
        import aws_sdk_eventbridge.types.header_parameters_map

        out["header_parameters"] = (
            aws_sdk_eventbridge.types.header_parameters_map.deserialize_aws_json_1_1(
                data["HeaderParameters"]
            )
        )
    if "QueryStringParameters" in data:
        import aws_sdk_eventbridge.types.query_string_parameters_map

        out["query_string_parameters"] = (
            aws_sdk_eventbridge.types.query_string_parameters_map.deserialize_aws_json_1_1(
                data["QueryStringParameters"]
            )
        )
    return out
