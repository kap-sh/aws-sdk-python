"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionHttpParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.connection_body_parameters_list
    import aws_sdk_eventbridge.types.connection_header_parameters_list
    import aws_sdk_eventbridge.types.connection_query_string_parameters_list


class ConnectionHttpParameters(TypedDict):
    header_parameters: NotRequired[
        "aws_sdk_eventbridge.types.connection_header_parameters_list.ConnectionHeaderParametersList"
    ]
    """<p>Any additional header parameters for the connection.</p>"""
    query_string_parameters: NotRequired[
        "aws_sdk_eventbridge.types.connection_query_string_parameters_list.ConnectionQueryStringParametersList"
    ]
    """<p>Any additional query string parameters for the connection.</p>"""
    body_parameters: NotRequired[
        "aws_sdk_eventbridge.types.connection_body_parameters_list.ConnectionBodyParametersList"
    ]
    """<p>Any additional body string parameters for the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionHttpParameters) -> dict:
    out: dict = {}
    if "header_parameters" in value:
        import aws_sdk_eventbridge.types.connection_header_parameters_list

        out["HeaderParameters"] = (
            aws_sdk_eventbridge.types.connection_header_parameters_list.serialize_aws_json_1_1(
                value["header_parameters"]
            )
        )
    if "query_string_parameters" in value:
        import aws_sdk_eventbridge.types.connection_query_string_parameters_list

        out["QueryStringParameters"] = (
            aws_sdk_eventbridge.types.connection_query_string_parameters_list.serialize_aws_json_1_1(
                value["query_string_parameters"]
            )
        )
    if "body_parameters" in value:
        import aws_sdk_eventbridge.types.connection_body_parameters_list

        out["BodyParameters"] = (
            aws_sdk_eventbridge.types.connection_body_parameters_list.serialize_aws_json_1_1(
                value["body_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionHttpParameters:
    out: ConnectionHttpParameters = {}  # type: ignore[typeddict-item]
    if "HeaderParameters" in data:
        import aws_sdk_eventbridge.types.connection_header_parameters_list

        out["header_parameters"] = (
            aws_sdk_eventbridge.types.connection_header_parameters_list.deserialize_aws_json_1_1(
                data["HeaderParameters"]
            )
        )
    if "QueryStringParameters" in data:
        import aws_sdk_eventbridge.types.connection_query_string_parameters_list

        out["query_string_parameters"] = (
            aws_sdk_eventbridge.types.connection_query_string_parameters_list.deserialize_aws_json_1_1(
                data["QueryStringParameters"]
            )
        )
    if "BodyParameters" in data:
        import aws_sdk_eventbridge.types.connection_body_parameters_list

        out["body_parameters"] = (
            aws_sdk_eventbridge.types.connection_body_parameters_list.deserialize_aws_json_1_1(
                data["BodyParameters"]
            )
        )
    return out
