"""Generated from Smithy shape ``com.amazonaws.route53#CreateQueryLoggingConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.query_logging_config
    import aws_sdk_route_53.types.resource_uri


class CreateQueryLoggingConfigResponse(TypedDict):
    query_logging_config: (
        "aws_sdk_route_53.types.query_logging_config.QueryLoggingConfig"
    )
    """<p>A complex type that contains the ID for a query logging configuration, the ID of the hosted zone that you want to log queries for, and the ARN for the log group that you want Amazon Route 53 to send query logs to.</p>"""
    location: "aws_sdk_route_53.types.resource_uri.ResourceURI"
    """<p>The unique URL representing the new query logging configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateQueryLoggingConfigResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.query_logging_config

    aws_sdk_route_53.types.query_logging_config.serialize_xml(
        value["query_logging_config"], el, "QueryLoggingConfig"
    )


def deserialize_xml(el: Element) -> CreateQueryLoggingConfigResponse:
    out: CreateQueryLoggingConfigResponse = {}  # type: ignore[typeddict-item]
    child_query_logging_config = el.find("QueryLoggingConfig")
    if child_query_logging_config is not None:
        import aws_sdk_route_53.types.query_logging_config

        out["query_logging_config"] = (
            aws_sdk_route_53.types.query_logging_config.deserialize_xml(
                child_query_logging_config
            )
        )
    else:
        raise DeserializationError(
            "CreateQueryLoggingConfigResponse.query_logging_config required"
        )
    return out
