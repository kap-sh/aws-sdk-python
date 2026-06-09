"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopePathRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.path_statement_request
    import aws_sdk_ec2.types.through_resources_statement_request_list


class AccessScopePathRequest(TypedDict):
    source: NotRequired["aws_sdk_ec2.types.path_statement_request.PathStatementRequest"]
    """<p>The source.</p>"""
    destination: NotRequired[
        "aws_sdk_ec2.types.path_statement_request.PathStatementRequest"
    ]
    """<p>The destination.</p>"""
    through_resources: NotRequired[
        "aws_sdk_ec2.types.through_resources_statement_request_list.ThroughResourcesStatementRequestList"
    ]
    """<p>The through resources.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccessScopePathRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source" in value:
        import aws_sdk_ec2.types.path_statement_request

        aws_sdk_ec2.types.path_statement_request.serialize_ec2_query(
            value["source"], pairs, f"{prefix}.Source"
        )
    if "destination" in value:
        import aws_sdk_ec2.types.path_statement_request

        aws_sdk_ec2.types.path_statement_request.serialize_ec2_query(
            value["destination"], pairs, f"{prefix}.Destination"
        )
    if "through_resources" in value:
        import aws_sdk_ec2.types.through_resources_statement_request_list

        aws_sdk_ec2.types.through_resources_statement_request_list.serialize_ec2_query(
            value["through_resources"], pairs, f"{prefix}.ThroughResources"
        )


def deserialize_ec2_query(el: Element) -> AccessScopePathRequest:
    out: AccessScopePathRequest = {}  # type: ignore[typeddict-item]
    child_source = el.find("Source")
    if child_source is not None:
        import aws_sdk_ec2.types.path_statement_request

        out["source"] = aws_sdk_ec2.types.path_statement_request.deserialize_ec2_query(
            child_source
        )
    child_destination = el.find("Destination")
    if child_destination is not None:
        import aws_sdk_ec2.types.path_statement_request

        out["destination"] = (
            aws_sdk_ec2.types.path_statement_request.deserialize_ec2_query(
                child_destination
            )
        )
    if el.find("ThroughResources") is not None:
        import aws_sdk_ec2.types.through_resources_statement_request_list

        out["through_resources"] = (
            aws_sdk_ec2.types.through_resources_statement_request_list.deserialize_ec2_query(
                el, "ThroughResources"
            )
        )
    return out
