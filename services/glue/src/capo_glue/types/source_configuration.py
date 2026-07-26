"""Generated from Smithy shape ``com.amazonaws.glue#SourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connector_property_list
    import capo_glue.types.http_method
    import capo_glue.types.pagination_configuration
    import capo_glue.types.path_string
    import capo_glue.types.response_configuration


class SourceConfiguration(TypedDict, closed=True):
    request_method: NotRequired["capo_glue.types.http_method.HTTPMethod"]
    """<p>The HTTP method to use for requests to this endpoint, such as GET, POST.</p>"""
    request_path: NotRequired["capo_glue.types.path_string.PathString"]
    """<p>The URL path for the REST endpoint, which may include parameter placeholders that will be replaced with actual values during requests.</p>"""
    request_parameters: NotRequired[
        "capo_glue.types.connector_property_list.ConnectorPropertyList"
    ]
    """<p>Configuration for request parameters that should be included in API calls, such as query parameters, headers, or body content.</p>"""
    response_configuration: NotRequired[
        "capo_glue.types.response_configuration.ResponseConfiguration"
    ]
    """<p>Configuration that defines how to parse and extract data from API responses, including success and error handling.</p>"""
    pagination_configuration: NotRequired[
        "capo_glue.types.pagination_configuration.PaginationConfiguration"
    ]
    """<p>Configuration for handling paginated responses from the REST API, supporting both cursor-based and offset-based pagination strategies.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceConfiguration) -> dict:
    out: dict = {}
    if "request_method" in value:
        import capo_glue.types.http_method

        out["RequestMethod"] = capo_glue.types.http_method.serialize_aws_json_1_1(
            value["request_method"]
        )
    if "request_path" in value:
        out["RequestPath"] = value["request_path"]
    if "request_parameters" in value:
        import capo_glue.types.connector_property_list

        out["RequestParameters"] = (
            capo_glue.types.connector_property_list.serialize_aws_json_1_1(
                value["request_parameters"]
            )
        )
    if "response_configuration" in value:
        import capo_glue.types.response_configuration

        out["ResponseConfiguration"] = (
            capo_glue.types.response_configuration.serialize_aws_json_1_1(
                value["response_configuration"]
            )
        )
    if "pagination_configuration" in value:
        import capo_glue.types.pagination_configuration

        out["PaginationConfiguration"] = (
            capo_glue.types.pagination_configuration.serialize_aws_json_1_1(
                value["pagination_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceConfiguration:
    out: SourceConfiguration = {}  # type: ignore[typeddict-item]
    if "RequestMethod" in data:
        import capo_glue.types.http_method

        out["request_method"] = capo_glue.types.http_method.deserialize_aws_json_1_1(
            data["RequestMethod"]
        )
    if "RequestPath" in data:
        out["request_path"] = data["RequestPath"]
    if "RequestParameters" in data:
        import capo_glue.types.connector_property_list

        out["request_parameters"] = (
            capo_glue.types.connector_property_list.deserialize_aws_json_1_1(
                data["RequestParameters"]
            )
        )
    if "ResponseConfiguration" in data:
        import capo_glue.types.response_configuration

        out["response_configuration"] = (
            capo_glue.types.response_configuration.deserialize_aws_json_1_1(
                data["ResponseConfiguration"]
            )
        )
    if "PaginationConfiguration" in data:
        import capo_glue.types.pagination_configuration

        out["pagination_configuration"] = (
            capo_glue.types.pagination_configuration.deserialize_aws_json_1_1(
                data["PaginationConfiguration"]
            )
        )
    return out
