"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopePathRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.path_statement_request
    import capo_ec2.types.through_resources_statement_request_list


class AccessScopePathRequest(TypedDict, closed=True):
    source: NotRequired["capo_ec2.types.path_statement_request.PathStatementRequest"]
    """<p>The source.</p>"""
    destination: NotRequired[
        "capo_ec2.types.path_statement_request.PathStatementRequest"
    ]
    """<p>The destination.</p>"""
    through_resources: NotRequired[
        "capo_ec2.types.through_resources_statement_request_list.ThroughResourcesStatementRequestList"
    ]
    """<p>The through resources.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccessScopePathRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source" in value:
        import capo_ec2.types.path_statement_request

        capo_ec2.types.path_statement_request.serialize_ec2_query(
            value["source"], pairs, f"{key_prefix}Source"
        )
    if "destination" in value:
        import capo_ec2.types.path_statement_request

        capo_ec2.types.path_statement_request.serialize_ec2_query(
            value["destination"], pairs, f"{key_prefix}Destination"
        )
    if "through_resources" in value:
        import capo_ec2.types.through_resources_statement_request_list

        capo_ec2.types.through_resources_statement_request_list.serialize_ec2_query(
            value["through_resources"], pairs, f"{key_prefix}ThroughResource"
        )


def deserialize_ec2_query(el: Element) -> AccessScopePathRequest:
    out: AccessScopePathRequest = {}  # type: ignore[typeddict-item]
    child_source = el.find("Source")
    if child_source is not None:
        import capo_ec2.types.path_statement_request

        out["source"] = capo_ec2.types.path_statement_request.deserialize_ec2_query(
            child_source
        )
    child_destination = el.find("Destination")
    if child_destination is not None:
        import capo_ec2.types.path_statement_request

        out["destination"] = (
            capo_ec2.types.path_statement_request.deserialize_ec2_query(
                child_destination
            )
        )
    child_through_resources = el.find("ThroughResource")
    if child_through_resources is not None:
        import capo_ec2.types.through_resources_statement_request_list

        out["through_resources"] = (
            capo_ec2.types.through_resources_statement_request_list.deserialize_ec2_query(
                child_through_resources
            )
        )
    return out
