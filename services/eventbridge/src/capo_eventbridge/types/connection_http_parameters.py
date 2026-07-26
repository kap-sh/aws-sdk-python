"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionHttpParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.connection_body_parameters_list
    import capo_eventbridge.types.connection_header_parameters_list
    import capo_eventbridge.types.connection_query_string_parameters_list


class ConnectionHttpParameters(TypedDict, closed=True):
    header_parameters: NotRequired[
        "capo_eventbridge.types.connection_header_parameters_list.ConnectionHeaderParametersList"
    ]
    """<p>Any additional header parameters for the connection.</p>"""
    query_string_parameters: NotRequired[
        "capo_eventbridge.types.connection_query_string_parameters_list.ConnectionQueryStringParametersList"
    ]
    """<p>Any additional query string parameters for the connection.</p>"""
    body_parameters: NotRequired[
        "capo_eventbridge.types.connection_body_parameters_list.ConnectionBodyParametersList"
    ]
    """<p>Any additional body string parameters for the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionHttpParameters) -> dict:
    out: dict = {}
    if "header_parameters" in value:
        import capo_eventbridge.types.connection_header_parameters_list

        out["HeaderParameters"] = (
            capo_eventbridge.types.connection_header_parameters_list.serialize_aws_json_1_1(
                value["header_parameters"]
            )
        )
    if "query_string_parameters" in value:
        import capo_eventbridge.types.connection_query_string_parameters_list

        out["QueryStringParameters"] = (
            capo_eventbridge.types.connection_query_string_parameters_list.serialize_aws_json_1_1(
                value["query_string_parameters"]
            )
        )
    if "body_parameters" in value:
        import capo_eventbridge.types.connection_body_parameters_list

        out["BodyParameters"] = (
            capo_eventbridge.types.connection_body_parameters_list.serialize_aws_json_1_1(
                value["body_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionHttpParameters:
    out: ConnectionHttpParameters = {}  # type: ignore[typeddict-item]
    if "HeaderParameters" in data:
        import capo_eventbridge.types.connection_header_parameters_list

        out["header_parameters"] = (
            capo_eventbridge.types.connection_header_parameters_list.deserialize_aws_json_1_1(
                data["HeaderParameters"]
            )
        )
    if "QueryStringParameters" in data:
        import capo_eventbridge.types.connection_query_string_parameters_list

        out["query_string_parameters"] = (
            capo_eventbridge.types.connection_query_string_parameters_list.deserialize_aws_json_1_1(
                data["QueryStringParameters"]
            )
        )
    if "BodyParameters" in data:
        import capo_eventbridge.types.connection_body_parameters_list

        out["body_parameters"] = (
            capo_eventbridge.types.connection_body_parameters_list.deserialize_aws_json_1_1(
                data["BodyParameters"]
            )
        )
    return out
